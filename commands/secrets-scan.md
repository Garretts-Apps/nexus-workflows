---
description: Scan the tree for committed secrets and risky assignments
---

# Secrets scan

Scope: $ARGUMENTS

No scope given? The working tree, plus the history of the current branch. Say which.

A secret that ever reached a remote is leaked, even if the next commit deleted it. The scan finds them; rotation is what fixes them.

- **Use the scanner CI already runs,** if any. Otherwise `python3 scripts/scan_secrets.py --report <path>` from this kit.
- **Scan history too** for anything that was pushed: a secret removed in a later commit is still in the clone.
- Triage each hit: real credential, test fixture, placeholder, or false positive. Say why for each. The kit's scanner lists test and fixture hits last, marked `:test`; a fake key in a test is still worth a glance, since real ones get pasted there too.
- **Never print the value.** Path, line and kind only.
- For a real one: it needs rotating at the provider, then removing. Rotation and history rewrites are the owner's call and outward-facing: **ask**, and recommend rotating first.
- Add the guard that would have caught it (pre-commit hook, CI step), if the repo lacks one.

**Done when** every hit is triaged with a reason and no value appears anywhere in the report.
