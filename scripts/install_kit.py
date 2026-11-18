#!/usr/bin/env python3
"""Copy the kit into the folders a harness reads. Stdlib only.

    python3 scripts/install_kit.py --layout bwn --dry-run
    python3 scripts/install_kit.py --layout claude --into ~/code/my-app
    python3 scripts/install_kit.py --layout agents --into . --only skills

Layouts:
  bwn     commands/ skills/ agents/ into <into>, scripts/ into <into>/hooks
          (<into> defaults to ~/.buildwithnexus)
  claude  everything under <into>/.claude/  (scripts/ as .claude/scripts)
  agents  everything under <into>/.agents/

--hooks (bwn only) also puts the guards where bwn finds them on its own,
one event folder each: hooks/PreToolUse/guard_shell.py, guard_writes.py,
hooks/UserPromptSubmit/screen_prompt.py, hooks/PostToolUse/strip_invisible.py.
That turns them on; leave it off and nothing runs until you wire it.

It never deletes, and it never replaces a file you changed: a target that
differs from the kit is skipped and reported unless you pass --force.
Prints one line per file (copy, same, skip, replace) and a count.
"""
import argparse
import filecmp
import shutil
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
PARTS = ("commands", "skills", "agents", "scripts")
# bwn runs any script in ~/.buildwithnexus/hooks/<Event>/ for every tool call.
BWN_EVENTS = {
    "guard_shell.py": "PreToolUse",
    "guard_writes.py": "PreToolUse",
    "screen_prompt.py": "UserPromptSubmit",
    "strip_invisible.py": "PostToolUse",
}


def destinations(layout, into):
    if layout == "bwn":
        return {"commands": into / "commands", "skills": into / "skills",
                "agents": into / "agents", "scripts": into / "hooks"}
    root = into / (".claude" if layout == "claude" else ".agents")
    return {part: root / part for part in PARTS}


def sources(part):
    base = KIT / part
    for path in sorted(base.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if part == "scripts" and path.name in {"check_kit.py", "install_kit.py", "build_index.py"}:
            continue  # kit maintenance, not something a harness runs
        yield path, path.relative_to(base)


def plan(layout, into, only, force, hooks=False):
    if hooks:
        for name, event in BWN_EVENTS.items():
            yield decide(KIT / "scripts" / name, into / "hooks" / event / name, force)
    for part in only:
        target_root = destinations(layout, into)[part]
        for src, rel in sources(part):
            yield decide(src, target_root / rel, force)


def decide(src, dst, force):
    if not dst.exists():
        return "copy", src, dst
    if filecmp.cmp(src, dst, shallow=False):
        return "same", src, dst
    return ("replace" if force else "skip"), src, dst


def main(argv):
    parser = argparse.ArgumentParser(description="Copy the kit into a harness's folders.")
    parser.add_argument("--layout", choices=("bwn", "claude", "agents"), required=True)
    parser.add_argument("--into", type=Path, help="target root (bwn default: ~/.buildwithnexus)")
    parser.add_argument("--only", default=",".join(PARTS), help="comma list of: " + ", ".join(PARTS))
    parser.add_argument("--dry-run", action="store_true", help="print the plan, write nothing")
    parser.add_argument("--force", action="store_true", help="replace files that differ from the kit")
    parser.add_argument("--hooks", action="store_true", help="bwn only: also turn the guards on in hooks/<Event>/")
    args = parser.parse_args(argv)

    only = [p.strip() for p in args.only.split(",") if p.strip()]
    unknown = [p for p in only if p not in PARTS]
    if unknown:
        parser.error("unknown part(s): " + ", ".join(unknown))
    if args.into is None:
        if args.layout != "bwn":
            parser.error("--into is required for this layout")
        args.into = Path.home() / ".buildwithnexus"
    if args.hooks and args.layout != "bwn":
        parser.error("--hooks is for --layout bwn; other layouts wire hooks in their settings file")
    into = args.into.expanduser().resolve()

    counts = {"copy": 0, "same": 0, "skip": 0, "replace": 0}
    for action, src, dst in plan(args.layout, into, only, args.force, args.hooks):
        counts[action] += 1
        note = "  (differs from the kit; --force replaces it)" if action == "skip" else ""
        print(f"{action:8} {dst}{note}")
        if args.dry_run or action in ("same", "skip"):
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    summary = ", ".join(f"{n} {a}" for a, n in counts.items() if n)
    print(("dry run: " if args.dry_run else "") + (summary or "nothing to do"))
    if args.layout == "bwn" and "commands" in only:
        print("note: bwn answers /commit, /review, /pr and /debug itself; the kit's files of those names run headless only")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
