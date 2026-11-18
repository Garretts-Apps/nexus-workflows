---
name: api-design
description: Use when adding or changing a public interface (HTTP, RPC or library exports): contracts, errors, versioning, limits
---

# API design

**Use when** something outside this code will call it: an HTTP route, an RPC method, a library export, a CLI flag someone scripts against.

An API is a promise you can't take back quietly. Design for the caller who will depend on your mistakes.

## The contract

- **Name things in the caller's language,** not your table names. Nouns for resources, verbs only when it really is an action.
- **Errors are part of the interface:** a stable machine-readable code, a human message, and enough detail to fix the request. Never only a status code. Never a stack trace.
- **Be strict in what you accept** at first. Rejecting unknown fields is easy to relax later; accepting junk is impossible to tighten.
- **Idempotency for writes** that might be retried: an idempotency key, or PUT-style semantics. Networks retry whether you planned for it or not.
- **Pagination with a hard maximum,** cursor-based when data changes underneath. Totals only when they're cheap.
- **Time and money:** ISO 8601 with offsets, amounts as integers in minor units or decimals as strings, currency always named.

## Change

- **Additive changes are free; everything else is a version.** Removing a field, tightening validation, changing a default and changing an error code all break someone.
- Deprecate with a date and a replacement, and say so in the response, not just the docs.

## Defaults that matter

- Auth required unless deliberately public. Authorization checked per object, not per route.
- Rate limits, size limits and timeouts documented and enforced.
- Secrets never echoed back, in errors or logs.

## Documentation

Every operation: inputs, outputs, errors, auth, limits, and one example that actually works. `/api-docs` writes it from the code.

**Done when** the contract covers errors and limits, the change is additive or versioned, and an example request has been run.
