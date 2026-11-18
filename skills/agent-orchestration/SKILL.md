---
name: agent-orchestration
description: Use when splitting work across helpers: who gets what, what they return, and how to trust it
---

# Agent orchestration

**Use when** a job splits into parts that don't depend on each other, or one part needs a fresh pair of eyes that hasn't read your conclusion.

Delegation saves time only if the handoff is cheap and the result is checkable. Most of the cost is in the brief and the merge, not the work.

## Splitting

- **Split by independence, not by size.** Two parts that need each other's answers belong to one helper, or to you.
- **One outcome per helper.** Give it the goal, the paths in scope, what's off limits, and what done looks like. It knows only what you wrote.
- **Read-only helpers run in parallel; writers run one at a time.** Two helpers editing the same tree is a merge conflict with extra steps.
- Don't hand a helper your hypothesis to confirm. It will.

## What comes back

- **Fix the report shape** in the brief: findings with `path:line`, severity, and what wasn't checked. Prose comes back as prose.
- **Verify before you repeat it.** A helper's finding is a lead until you've opened the file. Mistakes arrive in the same confident tone as facts.
- Merge: dedupe, resolve contradictions by reading the code, and say which helper found what.

## When it goes wrong

A helper that errors or times out leaves a hole. Say what wasn't covered. Don't round a partial result up to "checked everything".

**Done when** every helper's result is merged or marked missing, and each claim you pass on has been checked against the source.
