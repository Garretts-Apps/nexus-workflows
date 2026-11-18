---
description: Run every command block in a clean matching cell before handing it to the maintainer
---

# Rehearse

Blocks: $ARGUMENTS

No blocks given? Take the command blocks from your last reply, or from the Markdown file the working diff changed (install docs, a runbook, a README). Say which.

Load the `rehearse` skill and follow it. The short version: nothing goes to the maintainer that hasn't run somewhere that looks like their machine.

- Lint first: `python3 scripts/lint_blocks.py <file.md>` for the `# expect:` rule.
- Run each block in a fresh shell in a matching cell, in order, and compare the output to its `# expect:` line.
- Fix and re-run a failing block. Don't hand it over with a warning attached.
- **Ask** only for facts about their machine that change the blocks (OS edition, shell, elevation, runtime manager), once, with defaults offered. No answer means the hardest case.

**Done when** each block's rehearsal output is quoted next to its `# expect:` line, or the block is listed under `Not rehearsed:` with the reason.
