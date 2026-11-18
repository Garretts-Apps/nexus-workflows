---
description: Find generated-code leftovers and repair them in focused commits
---

# Deslop

Scope: $ARGUMENTS

No scope given? The working diff, else the branch against main, else the whole tree. Say which.

Load the `deslop` skill and follow it.

- `report`, `--report` or `dry-run` in the arguments: scan and report, no edits, no commits.
- `--ci`: run the Unicode scanner and stop. Its exit code is the answer.
- Otherwise report by severity, then fix in small commits, one category each, with the tests run after every commit.
- **When in doubt, keep it** and put it on the Kept list. Deleting something deliberate to tidy up is worse than the slop.
- **Ask** before removing anything that looks like a public API, a config default or a comment that explains a hack.

**Done when** the report is out, each fix commit has a quoted test run, and the Kept list is there.
