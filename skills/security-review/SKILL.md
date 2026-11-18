---
name: security-review
description: Use when reviewing code for security: trace untrusted input to dangerous sinks, check authorization, prove each finding
---

# Security review

**Use when** a change touches input handling, auth, secrets, file or network access, deserialization, shell or query construction, hooks, or anything an outsider can reach. `/security-review` loads this.

Security review is following data you don't control to places where it can do damage, and proving the path exists. A list of scary words found by grep is not a review.

## Map first

- **Entry points:** request handlers, CLI arguments, environment, files read, webhooks, message queues, anything a model or another service sends you. In agent tooling, fetched content and tool output count: they can carry instructions.
- **Sinks:** shell, SQL and other query languages, file paths, templates and HTML, deserializers, redirects, outbound requests, `eval` in any form.
- **Trust boundaries:** where data crosses from less trusted to more trusted. That's where checks belong.

## What to look for

- **Injection:** untrusted data reaching a sink without parameterization or a strict allowlist. Escaping by hand is a finding.
- **Authorization:** checked on every handler, against the specific object, not just "is logged in". Missing checks hide in the second, less popular route to the same data.
- **Paths:** normalized and resolved before the check, then checked against the allowed root. Symlinks and `..` are the classics.
- **Secrets:** in code, config, URLs, logs, error messages, CI output. A key that reached a remote is leaked; removal isn't enough, it needs rotating.
- **Defaults that fail open:** debug on, verification off, permissive CORS, wildcard allowlists, "temporary" bypasses.
- **Outbound requests** that a user can steer to internal addresses.
- **Dependencies** only where a known issue is reachable from this code; `/deps-audit` covers the rest.
- **Mutating actions** behind a confirmation or permission gate, especially in tools that agents drive.

## Prove it

Each finding gets: severity, `path:line`, the path an attacker takes to reach it (entry point to sink), the impact, and a minimal fix. If you can't show a path, it's a suspicion; label it that way.

Use scanners the repo already runs; don't install new ones for a review. Large diffs can be split with the read-only `security-check` helper. A new trust boundary also deserves `/threat-model`.

## What not to do

No compliance claims. No edits unless a fix was asked for. Rotating a real credential is the owner's decision: ask, and recommend rotating first.

**Done when** each finding has a location, a reachable path and a fix, unproven ones are labeled, and the review says what was out of scope.
