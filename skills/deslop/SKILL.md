---
name: deslop
description: Use after heavy generated edits: find the debris (invisible Unicode, narrating comments, dead code, stock prose), rank it, and clean it up in small commits
---

# Deslop

**Use when** a lot of code or prose was just generated, or something reads like nobody in particular wrote it.

Remove residue that doesn't change behavior. When an edit might be deliberate, keep it and say so.

## 1. Scope and mode

Work the path the user named, or the full tree when they named none.

- `report` / `--report` / `dry-run`: scan, print, exit without edits or commits.
- `--ci`: run `scripts/scan_slop.py --ci` only; a non-zero exit is the deliverable.
- Otherwise: scan, report, then fix.

## 2. Unicode scanner

Use `scripts/scan_slop.py` from this kit (or the same file copied into your agent scripts directory).

```
python3 scripts/scan_slop.py --report
python3 scripts/scan_slop.py --ci
```

Each hit is `file:line:U+XXXX`. `--ci` fails only on invisible Unicode (U+200B-U+200D, U+2060, stray BOM, bidi controls, tag characters U+E0000-U+E007F). Smart quotes, dashes, NBSP, and line separators are reported in `--report` and do not fail `--ci`.

## 3. Report ranks

Blocker: invisible or bidi characters in code, swallowed errors, debug prints, placeholder data on shipped paths, imports the build rejects.

Should-fix: narrating comments, commented-out code, TODOs with no owner, stock doc phrasing, stray `.bak`/`.tmp`, duplicate tool configs.

Note: smart punctuation in prose, long but straight functions, exports you cannot prove unused.

End with a Kept list. In `--report` and `--ci`, stop after the report.

## 4. Fix order

When edits are allowed: unicode, comments, repo artifacts, formatting, writing, code smells, design. One commit per category with subject `deslop: <category>`. Run the project's tests after each commit and quote the result. Do not amend or push.

When the tree has UI, read `distinctive-design` and report generated-default patterns. Fix design only in a design commit for the screen in scope.

**Done when** the report is out, each fix category is its own commit with a quoted test run, and the Kept list is there.
