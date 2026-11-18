# CI examples (opt-in)

Copy workflows into `.github/workflows/` and tune triggers. They use upstream actions; nothing runs until you enable them in GitHub.

| File | Purpose |
| --- | --- |
| `secret-scan.yml` | TruffleHog on push and pull_request |
| `dependency-audit.yml` | Ecosystem audits via matrix (Node, Rust, Python) |
| `codeql-analysis.yml` | CodeQL init/analyze for JavaScript and Python (add `java-kotlin` and a build step if you need it) |

All three run on `ubuntu-latest` with a read-only token. Actions are pinned to tags; pin them to commit SHAs if your policy requires it (the `pipeline-reviewer` agent flags tags).