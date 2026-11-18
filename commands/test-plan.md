---
description: Outline test scope, types, and risks from requirements
---

# Test plan

Scope: $ARGUMENTS

No scope given? The feature or change on the branch, from its spec, issue or diff. Say which.

A test plan decides where testing effort goes. Everything can't be tested, so say what won't be, on purpose.

- **List the behaviors that must be proven,** each with a priority based on what breaks if it's wrong, and for whom.
- **Pick the cheapest test that proves each:** unit for logic, integration for seams, end-to-end only for the paths that need a real browser or a real system.
- **Risk table:** what could go wrong, likelihood, impact, and the test that covers it, or "accepted, not tested" with a reason.
- Data, environments and tooling the repo already has; name gaps, don't assume new infrastructure.
- Plan only. Writing the tests is `/test` or `/testgen`.
- **Ask** only for priorities the code can't reveal: which users matter most, what can't break on launch.

**Done when** every listed behavior has a test type or an explicit "not tested, because".
