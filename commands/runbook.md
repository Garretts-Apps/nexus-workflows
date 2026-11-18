---
description: Write an operator runbook for running and fixing the service
---

# Runbook

Service: $ARGUMENTS

No service given? The main deployable in the repo. Say which.

Write for the person paged at 2am who didn't write the code and is mildly annoyed about it. Commands they can paste, not paragraphs they have to interpret.

- **Start, stop, restart, health check,** each as a command with the output that means "fine".
- **Where to look:** logs, metrics, dashboards, by name and path.
- **Top failure modes** from code, past incidents and error handling: symptom, how to confirm, safe mitigation, and what *not* to do.
- **Every mitigation is safe to try twice.** Anything destructive is marked, with how to undo it.
- **Escalation:** when to stop mitigating and who to call, by role.
- No secrets; say where they live. Prefer the repo's docs folder, e.g. `docs/runbooks/`.
- **Ask** only for things only operators know: on-call roles, dashboards outside the repo.

**Done when** each failure mode has a confirm step and a mitigation, and every command in the runbook is copy-pasteable.
