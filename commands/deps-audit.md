---
description: Run dependency vulnerability audits for this repo's ecosystem
---

# Dependency audit

Scope: $ARGUMENTS

No scope given? Every manifest and lockfile in the repo. Say which ecosystems you found.

An advisory is only urgent if the vulnerable code can run in your context. Sort that out before anyone panics.

- **Use the tool the project already runs** in CI or its docs. Otherwise the ecosystem's standard auditor, if installed. Don't install new tooling to answer a quick question; say what you couldn't run.
- **Triage each finding:** is the package in production or dev only? Is the vulnerable function reachable from our code? Is there a fixed version, and how far away is it?
- Separate "upgrade now" from "track" from "not reachable, note why". A wall of CVE IDs is not a report.
- Upgrades go one package at a time, with the tests run after each. **Major version bumps need a plan the maintainer agrees to:** ask, and recommend one.
- Lockfiles change with upgrades and never without them.

**Done when** each finding is marked upgrade, track or not-reachable with a reason, and any upgrade is followed by a quoted test run.
