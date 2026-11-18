---
description: Measure entropy hotspots and apply small verified cleanups
---

# Entropy

Scope: $ARGUMENTS

No scope given? The whole tree, minus dependencies and build output.

Entropy is code that costs more to change than it should. Measure first, because the file everyone complains about is rarely the one that hurts most.

- **Measure** with `python3 scripts/measure_entropy.py --report <path>`: big files, repeated blocks, churn. Churn times size is where the pain is.
- **Then read** what the script can't see: dead exports, unused flags, two helpers that do the same thing, abstractions with one caller.
- **Prefer deletion to rearrangement.** Removing dead code is the only refactor with no regression risk in the deleted part.
- **Default is report only.** If cleanup was asked for: one item per commit, behavior unchanged, tests run after each, revert on red.
- Replacing a whole subsystem is `/rebuild`, not this.
- **Ask** before touching public interfaces or anything another repo might import.

**Done when** there's a ranked list with file evidence, and any cleanup commits each have a quoted green test run.
