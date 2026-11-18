---
description: Review a change or path for security defects, with evidence
---

# Security review

Scope: $ARGUMENTS

No scope given? The working diff, else the branch against main, else the whole tree with the entry points first. Say which.

Load the `security-review` skill and work from it. The short version: follow untrusted data from where it enters to where it can do damage, and prove each finding.

- **Start at the edges:** request handlers, CLI arguments, file and network reads, webhooks, anything parsed. Then follow the data to shells, queries, paths, templates, deserializers and redirects.
- **Authorization at every handler,** not just authentication at the front door. Check the object, not just the user.
- **Secrets and logs:** keys in code or config, tokens in URLs, credentials in error messages and logs.
- **Defaults that fail open:** permissive CORS, debug on, verification off, wildcards in allowlists.
- **Dependencies** only where a known issue is reachable; run `/deps-audit` for the rest.
- A new trust boundary or a big feature also gets `/threat-model`. Large diffs can be split with the read-only `security-check` helper.
- Each finding: severity, `path:line`, how an attacker would reach it, and a minimal fix. Unproven suspicions are labeled as such.
- Fixes only if asked. A real secret means rotation, which is the owner's call: **ask**.

**Done when** each finding has a location, a reachable path and a fix, and you've named what was out of scope or not checked.
