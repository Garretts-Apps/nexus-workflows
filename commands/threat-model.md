---
description: List threats and mitigations for a feature or surface
---

# Threat model

Scope: $ARGUMENTS

No scope given? The newest trust boundary in the branch: a new endpoint, integration, file input or permission. Say which.

A threat model is a map of where trust changes hands, and what happens when someone lies at each handover.

- **Draw the boundary in words:** actors, entry points, data stores, and every place data crosses from less trusted to more trusted.
- **Walk each crossing:** who can pretend to be someone else, tamper with data, deny doing something, read what they shouldn't, exhaust it, or gain rights they shouldn't have.
- **Tie each threat to evidence** in code or config, or mark it as assumed.
- **Mitigations:** present (with the path), missing (with a fix), or accepted (with who accepted it). Rank by how reachable and how bad.
- The output is a table plus the boundary description. No certification language.
- Fixes only if asked. **Ask** only about deployment facts the repo can't show (who can reach it, what's in front of it).

**Done when** every crossing has its threats listed with evidence and a mitigation status.
