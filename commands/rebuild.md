---
description: Spec-driven rebuild in vertical slices with old and new paths in parallel
---

# Rebuild

Scope: $ARGUMENTS

No scope given? The subsystem `/entropy` would rank worst: big, churny and hard to change. Say which, and why.

A rebuild is replacing the engine while the car is on the motorway. The old path keeps running until the new one has proven itself on real behavior.

- **The existing behavior is the spec,** bugs included, until someone decides otherwise. Pin it with tests before touching anything. Undocumented behavior that callers rely on is still behavior.
- **Slice vertically** and keep old and new side by side behind a switch or a routing seam. Each slice moves real traffic or real callers, not a layer.
- **Compare outputs** where you can: run both, diff results, log mismatches. That catches what tests didn't think of.
- Delete the old path only after its slice has run clean, in a separate commit, so reverting is one step.
- Keep `spec/` notes short: the behavior contract, the slice plan, what's moved.
- **Ask** before deleting the old path, before changing behavior on purpose, and before any wide refactor.

**Done when** each moved slice has its contract tests green before and after, and the old path for it is either still running or deleted with the maintainer's okay.
