---
description: Produce a software bill of materials from manifests
---

# SBOM

Scope: $ARGUMENTS

No scope given? Everything shipped from this repo: every manifest and lockfile that ends up in a release. Say what you found.

An SBOM is only useful if it matches what was actually built. Generate it from lockfiles, not from memory.

- **Use the format and generator the repo already uses.** Otherwise the ecosystem's standard tool for a standard format, if installed. Say what you couldn't run.
- Direct and transitive dependencies, versions, and licenses where the metadata has them. Mark unknown licenses as unknown; don't guess.
- Separate what ships from dev-only tooling.
- Write it next to the release artifacts or under `docs/sbom/`, with the command that regenerates it.
- Publishing it is outward-facing: **ask** first.

**Done when** the SBOM file exists, its regenerate command is written down, and unknown licenses are listed.
