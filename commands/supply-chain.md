---
description: Review dependency provenance, pinning, and SBOM hygiene
---

# Supply chain

Scope: $ARGUMENTS

No scope given? The whole repo: manifests, lockfiles, CI, install scripts and container files. Say what you found.

Supply chain risk is mostly about what runs without anyone choosing it: an unpinned version, an install script, a mutable tag.

- **Lockfiles committed** and used in CI (`ci`-style installs, not resolving fresh every build).
- **Pinning:** dependencies, CI actions and base images by digest or commit where it matters. Moving tags are someone else's decision about your build.
- **Install-time code:** postinstall scripts, `curl | sh` in setup or Dockerfiles, downloads without checksums.
- **Provenance:** where packages come from, whether the build publishes attestations or checksums, whether anything verifies them.
- **SBOM and audit:** is there one, is it current? Use `/sbom` and `/deps-audit` rather than duplicating them.
- Output a short posture table (pinned, locked, audited, SBOM, CI gates, install-time code) with a fix per gap.
- **Ask** before changing anything in release or publish pipelines.

**Done when** each posture row has evidence or a gap with a fix.
