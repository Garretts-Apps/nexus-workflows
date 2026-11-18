---
description: Document a public HTTP or library API from the code that defines it
---

# API documentation

Scope: $ARGUMENTS

No scope given? Document whatever public surface the working diff or branch touched; with no diff, the whole public surface, shallowest first.

Docs are read by someone holding a failing request. Write for that person.

- **The code is the source of truth.** Read routers, handlers, schemas and exported types. Never document an endpoint you didn't find in code.
- Per entry point: how to call it, who may, what it takes, what it returns, **what it returns when it fails**, and one example that would actually work.
- **Errors and limits get equal billing** with the happy path: status codes, error shapes, rate limits, pagination caps, size limits.
- Mark what is stable and what is likely to change. Flag anything the code accepts but probably shouldn't.
- Use the format the repo already has (OpenAPI, README section, generated reference). With none, Markdown under `docs/api/`. If a spec file exists and disagrees with the code, say so; don't quietly pick one.
- **Ask** only when behavior is ambiguous in code and the docs would set a contract.

**Done when** every documented entry point traces to a file and line, and each has at least one failure case.
