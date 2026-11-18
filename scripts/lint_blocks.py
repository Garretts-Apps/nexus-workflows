#!/usr/bin/env python3
"""Check command blocks in Markdown before anyone rehearses them. Stdlib only.

    python3 scripts/lint_blocks.py docs/install.md [more.md ...]

Every fenced shell block (bash, sh, zsh, powershell, pwsh, ps1, cmd,
console) must end with an `# expect: <text>` line, optionally followed by
`# expect-exit: N|any`. A block must not contain a bare `exit` line, which
closes the window it was pasted into. Prints file:line: problem, exits 1 on
any problem, 0 when clean.
"""
import re
import sys
from pathlib import Path

SHELLS = {"bash", "sh", "zsh", "powershell", "pwsh", "ps1", "cmd", "bat", "console", "shell"}
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([\w-]*)")


def blocks(text):
    """Yield (start_line, lang, body_lines) for each fenced block."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if not m:
            i += 1
            continue
        fence, lang, start = m.group(2), m.group(3).lower(), i + 1
        body = []
        i += 1
        while i < len(lines) and not lines[i].strip().startswith(fence):
            body.append(lines[i])
            i += 1
        yield start, lang, body
        i += 1


def lint(path):
    problems = []
    for start, lang, body in blocks(Path(path).read_text(encoding="utf-8")):
        if lang not in SHELLS:
            continue
        tail = [ln.strip() for ln in body if ln.strip()]
        while tail and tail[-1].lower().startswith("# expect-exit:"):
            tail.pop()
        if not tail or not tail[-1].lower().startswith("# expect:"):
            problems.append(f"{path}:{start}: {lang} block does not end with '# expect: <text>'")
        elif not tail[-1].split(":", 1)[1].strip():
            problems.append(f"{path}:{start}: '# expect:' has no text to look for")
        for offset, line in enumerate(body, 1):
            if re.fullmatch(r"\s*exit(\s+\d+)?\s*", line):
                problems.append(f"{path}:{start + offset}: bare 'exit' closes the window it is pasted into")
    return problems


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[2].strip(), file=sys.stderr)
        return 2
    problems = []
    for name in argv:
        if not Path(name).is_file():
            print(f"missing: {name}", file=sys.stderr)
            return 2
        problems.extend(lint(name))
    for line in problems:
        print(line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
