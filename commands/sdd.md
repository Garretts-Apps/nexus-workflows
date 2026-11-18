---
description: Start new work spec-first with tests and vertical slices
---

# Spec-driven start

Goal: $ARGUMENTS

No goal given? The feature the branch or conversation is heading toward. Say which.

Spec first means writing down what "working" looks like before anyone falls in love with an implementation.

- **If the goal is fuzzy, stop** and run `/discovery` or `/brainstorm`. A spec for a vague goal is fiction with numbered headings.
- **The spec** (`spec/<slug>.md`): the behavior in plain words, numbered acceptance checks someone could run, and an out-of-scope list.
- **Tests from the checks,** failing, before production code. IDs match: `AC-3` in the spec is `AC-3` in the test name.
- **Slice vertically** (`spec/<slug>-plan.md`): each slice is a thin path to something you can demo. Riskiest first.
- Build one slice at a time, tests green after each. When behavior drifts, update the spec in the same commit.
- Unknowns are `TBD` with an owner. Never invent a stakeholder or a date.
- **Ask** for review between spec and code, unless the maintainer already said go.

**Done when** the spec's checks are each tied to a test, and the slices built so far have those tests green.
