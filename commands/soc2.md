---
description: Repo readiness table against public SOC 2 Trust Services Criteria (not an audit)
---

# SOC 2 readiness

Scope: $ARGUMENTS

No scope given? The Security category for this repo; add others only if the maintainer names them.

This is a readiness check from repository evidence. It is not an audit, a certification or an opinion, and the table says so at the top.

- **Evidence from the repo only:** access control in code and config, secret handling, logging, change control (branch protection hints, required reviews, CI gates), vulnerability checks, backup and retention docs, encryption settings in config and infrastructure code.
- **One table:** criterion topic, evidence (path or config), gap, suggested fix.
- Rows the repo can't show get "needs operator evidence" (policies, access reviews, ticketing, cloud console). That's most of SOC 2, and pretending otherwise is how readiness checks get people in trouble.
- Never invent control IDs, auditors, audit windows or account names.
- **Ask** which categories beyond Security apply, with Security-only as the recommendation if they're unsure.

**Done when** every row has evidence or is marked as needing operator evidence, and the not-an-audit line is at the top.
