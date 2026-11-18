---
description: Plan a library or runtime migration without editing yet
---

# Migration plan

Target: $ARGUMENTS

No target given? The most out-of-date dependency or runtime that has a supported newer version, preferring ones with security fixes. Say which.

A migration plan is mostly a list of the things that will break, in the order you'll find out.

- **Inventory first:** current versions, every call site, and anything that pins the old version indirectly (plugins, CI images, lockfiles, docs).
- **Read the upstream breaking changes** for every version you skip, not just the last one.
- **Order the work so main stays shippable:** compatibility shims or both versions side by side, then move call sites in small batches, then remove the old path.
- Name the test that proves each step, and the rollback for each step. "Revert the PR" counts if it's true.
- Flag the risky ones: data format changes, behavior changes the tests don't cover, anything with a deprecation that turns into removal.
- Plan only. Executing it is a separate ask.
- **Ask** only when the target version is a real choice (LTS vs latest, a fork vs upstream).

**Done when** the plan lists call sites, breaking changes, ordered steps each with a test and rollback, and the risks.
