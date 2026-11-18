---
name: security-review
description: Threat-model and review code for command execution, credential, hook, and prompt-injection risk
---

# Security Review

Use this skill for threat modeling, dependency risk, command execution risk, hook/plugin safety, credential handling, and prompt-injection-sensitive workflows.

## Workflow

1. Search the tree for risky patterns: secrets, shell execution, network fetches, deserialization, path traversal, auth, permissions.
2. Read the security-critical flows end to end.
3. Run native scanners only if the repo already installs or configures them.
4. Keep a checklist of the threat-model areas and mark each one covered or skipped.

## Review checklist

- Inputs are validated before filesystem, shell, or network actions.
- Paths are normalized and sensitive locations are protected.
- Hooks and commands are visible/auditable.
- Credentials are not logged, traced, or sent to non-HTTPS endpoints.
- Permission gates cover mutating and destructive operations.
- External content cannot silently instruct the agent to run unsafe commands.

## Related commands

- `/threat-model` for a new trust boundary or feature.
- `/secrets-scan` and `/deps-audit` for automated passes.
- `/supply-chain` for pinning, lockfiles, and SBOM posture (`/sbom` to generate).
- Delegate large diffs to the read-only `security-check` helper.
