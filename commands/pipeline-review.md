---
description: Review CI/CD definitions for security, reliability, and least privilege
---

# Pipeline review

Scope: $ARGUMENTS

No scope given? Every pipeline definition in the repo: `.github/workflows/`, `azure-pipelines.yml` and its templates, and anything they include. Say what you found.

A pipeline holds the keys to production and runs code from pull requests. Review it like it does.

- **Untrusted code with trusted credentials** is the big one: `pull_request_target` or fork builds that check out PR code, secrets exposed to steps that run it, caches shared between them.
- **Least privilege:** explicit `permissions`, short-lived OIDC over stored secrets, environments with approvals in front of deploys.
- **Pinning:** third-party actions and tasks pinned to a commit, not a moving tag.
- **Injection:** untrusted event fields (titles, branch names) interpolated straight into shell.
- **Reliability:** tests before deploy, timeouts, concurrency groups, retries that hide real failures, caches keyed so they can't poison a release.
- Rank findings blocker, should-fix, note, each with `path:line` and a minimal YAML fix. Large diffs can go to the read-only `pipeline-reviewer` helper.
- Service connections, variable groups and org secrets are outward-facing: **ask** before changing any.

**Done when** each finding has a location, the risk in one line and a proposed fix, and you've named what you couldn't see (org settings, branch protection).
