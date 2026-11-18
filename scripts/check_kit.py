#!/usr/bin/env python3
"""Check the kit before anyone trusts it. Stdlib only.

    python3 scripts/check_kit.py

Fails (exit 1) when:
- a command has no `description` frontmatter, no `**Done when**` line, or
  no line saying what it does when run with no arguments, or a skill has no `name`
  and `description`, or a helper agent has no `name`, `description` and
  `tools`;
- a skill's `name` does not match its folder, or it has no `**Use when**`
  or `**Done when**` line;
- prose uses a word from VOICE.md's "don't use" list, or names another
  tool as a reference point;
- a backticked kit path (`scripts/x.py`, `skills/x/SKILL.md`, `/command`)
  points at nothing;
- a Python script does not compile;
- the tests in tests/ fail.

Prints one line per problem and a last line with the count.
"""
import py_compile
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Marketing words. Whole words, any case.
BANNED = [
    "awesome", "superpowers?", "supercharg\\w*", "unleash\\w*", "seamless\\w*",
    "leverag\\w*", "robust", "curated", "battle-tested", "best practices",
    "game-changer", "cutting-edge", "powerful", "blazing", "revolutioni[sz]e\\w*",
    "elevate\\w*", "empower\\w*", "delve\\w*", "comprehensive", "magic(al)?",
    "agentic", "vendor-neutral",
]
# Other tools, as proper names. Case-sensitive so a text cursor is fine.
NAMES = [
    "Claude Code", "Cursor", "Codex", "Copilot", "Aider", "Windsurf",
    "OpenCode", "Gemini CLI", "Cline", "Continue.dev",
]
# Files that list the banned words on purpose.
VOICE_EXEMPT = {"VOICE.md", "scripts/check_kit.py", "tests/test_check_kit.py"}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def frontmatter(text):
    m = FRONTMATTER.match(text)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def rel(path):
    return path.relative_to(ROOT).as_posix()


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix in {".md", ".py", ".json", ".yml", ".yaml"}:
            yield path


def check_frontmatter(problems):
    for path in sorted((ROOT / "commands").glob("*.md")):
        fm = frontmatter(path.read_text(encoding="utf-8"))
        if not fm or not fm.get("description"):
            problems.append(f"{rel(path)}: no description frontmatter")
        text = path.read_text(encoding="utf-8")
        if "**Done when**" not in text:
            problems.append(f"{rel(path)}: no **Done when** line (VOICE.md: How a command reads)")
        if "given?" not in text:
            problems.append(f"{rel(path)}: no line saying what it does with no arguments (\"No X given? ...\")")
        # Harnesses replace $1..$9 with positional arguments, so "$40" in
        # prose turns into the fourth argument followed by a zero.
        body = path.read_text(encoding="utf-8")
        for i, line in enumerate(body.splitlines(), 1):
            if re.search(r"\$[1-9]", line) and "$ARGUMENTS" not in line:
                problems.append(f"{rel(path)}:{i}: `$<digit>` is a positional placeholder; spell the amount out")
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        fm = frontmatter(path.read_text(encoding="utf-8"))
        if not fm or not fm.get("name") or not fm.get("description"):
            problems.append(f"{rel(path)}: needs name and description frontmatter")
        elif fm["name"] != path.parent.name:
            problems.append(f"{rel(path)}: name {fm['name']!r} is not the folder name {path.parent.name!r}")
        text = path.read_text(encoding="utf-8")
        for marker in ("**Use when**", "**Done when**"):
            if marker not in text:
                problems.append(f"{rel(path)}: no {marker} line")
    for path in sorted((ROOT / "agents").glob("*.md")):
        fm = frontmatter(path.read_text(encoding="utf-8"))
        if not fm or not all(fm.get(k) for k in ("name", "description", "tools")):
            problems.append(f"{rel(path)}: needs name, description and tools frontmatter")


def check_voice(problems):
    banned = re.compile(r"\b(" + "|".join(BANNED) + r")\b", re.I)
    names = re.compile(r"\b(" + "|".join(re.escape(n) for n in NAMES) + r")\b")
    for path in text_files():
        if rel(path) in VOICE_EXEMPT:
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in banned.finditer(line):
                problems.append(f"{rel(path)}:{i}: banned word {m.group(0)!r} (VOICE.md)")
            for m in names.finditer(line):
                problems.append(f"{rel(path)}:{i}: names another tool {m.group(0)!r}; give the folder path instead")


def check_references(problems):
    commands = {p.stem for p in (ROOT / "commands").glob("*.md")}
    path_ref = re.compile(r"`((?:scripts|skills|agents|commands|hooks|tests|workflows-examples)/[\w./-]+)`")
    cmd_ref = re.compile(r"`/([a-z][a-z0-9-]*)`")
    for path in text_files():
        if path.suffix != ".md":
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in path_ref.finditer(line):
                target = m.group(1).rstrip("/")
                if not (ROOT / target).exists():
                    problems.append(f"{rel(path)}:{i}: `{target}` does not exist")
            for m in cmd_ref.finditer(line):
                if m.group(1) not in commands:
                    problems.append(f"{rel(path)}:{i}: `/{m.group(1)}` is not a command in commands/")


def check_python(problems):
    for path in sorted(ROOT.rglob("*.py")):
        if ".git" in path.parts:
            continue
        try:
            py_compile.compile(str(path), doraise=True, cfile=None)
        except py_compile.PyCompileError as error:
            problems.append(f"{rel(path)}: does not compile: {error.msg.strip()}")


def check_tests(problems):
    if not (ROOT / "tests").is_dir():
        return
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if run.returncode != 0:
        tail = "\n".join((run.stderr or run.stdout).strip().splitlines()[-15:])
        problems.append(f"tests failed:\n{tail}")


def main(argv):
    problems = []
    check_frontmatter(problems)
    check_voice(problems)
    check_references(problems)
    check_python(problems)
    if "--no-tests" not in argv:
        check_tests(problems)
    for line in problems:
        print(line)
    print(f"{len(problems)} problem(s)" if problems else "kit ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
