---
description: Draft a design RFC for a cross-cutting technical choice
---

# RFC

Decision: $ARGUMENTS

No decision given? The cross-cutting choice the branch or conversation keeps circling. Say which.

An RFC is for a choice that's expensive to reverse and touches more than one team or system. Smaller than that, write an `/adr`.

- **Problem and constraints first,** including the ones nobody likes saying out loud: budget, deadline, who maintains it after.
- **Non-goals** stop the comments from wandering. Write them.
- **Options, honestly.** At least two real ones plus "do nothing". For each: what it costs to build, to run, to change your mind later.
- **Recommendation with the deciding reason,** and the migration path from where things are today.
- What would make you revisit the decision, and how you'd notice.
- Follow the repo's RFC folder and naming; with none, `docs/rfc/YYYY-MM-DD-short-title.md`. Link related ADRs.
- **Ask** only about constraints you can't see in the repo (deadlines, staffing, budget).

**Done when** the RFC has options with costs, a recommendation with its reason, non-goals and a migration path.
