---
name: rehearse
description: Use before handing the maintainer any command block to run on their own machine: run every block in a clean cell that matches theirs first
---

# Rehearse

**Use when** you are about to give the maintainer commands to run on their machine: install, setup, upgrade, triage, a one-liner "just paste this". Also before calling a platform or install fix done.

The maintainer is not the test environment. A block nobody ran is a guess, and the maintainer finds out by losing an afternoon.

## Deliverable first

Write one line: `Deliverable: <what they will have, on which machine, as which user, in which shell>`. Then read their request against it. Half of the bad blocks are good blocks for the wrong deliverable.

## Know the machine

Ask only what changes the blocks, once, with defaults offered:

- OS and edition (a server edition is not the desktop one), shell and its version.
- Elevated or not. Being in the admin group is not the same as running elevated.
- What manages the language runtime (a version manager, a system package, an installer), and what security software runs.

Unanswered means the hardest case. Rehearse for that.

## Write blocks that survive pasting

- **Numbered, one job each, standalone.** No block relies on a `cd`, a variable or a background process from an earlier one. Every block runs as if in a new window.
- **Each ends with a check** and an `# expect: <literal text>` line inside the fence. When failure is the point, add `# expect-exit: N`.
- No `exit` (it closes their window), no long scripts with `set -e`, no PATH change without a check in the next block that proves it took.
- Prefer blocks already in the project's docs, verbatim, if they've been rehearsed. A tweak is a new block.

`python3 scripts/lint_blocks.py <file.md>` checks the `# expect:` rule before you rehearse anything.

## Rehearse in a cell

A cell is a clean machine or container matching theirs: same OS family, shell, user rights and runtime manager. Run each block in a fresh shell, in order, and compare the output to its `# expect:` line.

- No matching cell? Say so: `Not rehearsed: <block> on <environment>, because <reason>`. That's information, not a task for the maintainer.
- A block that failed in the cell gets fixed and rehearsed again, not handed over with a warning.

## Hand over

Blocks in order, each with what it does in one line and what they should see. Then the `Not rehearsed:` list, if any.

**Done when** every handed-over block passed in a matching cell, or is listed under Not rehearsed with the reason.
