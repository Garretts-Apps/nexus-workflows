---
description: Report defects in the local diff by severity
---

# Review

Focus: $ARGUMENTS

No focus given? Review the working diff, else the branch against its base, else the last commit. Say which.

Read for behavior. Style is the formatter's job and it doesn't need your help.

- **Start with intent.** What is the change for? Does it do that? What else does it do?
- **Bugs live at the edges:** empty, one, many, concurrent, the failure path, retries, units and time zones, off-by-one, null.
- **Read past the diff.** Callers of what changed, config, migrations, and docs that are now quietly wrong.
- **Errors:** swallowed, logged-and-continued, retried forever. Each is a decision; check someone made it.
- **Untrusted input** reaching a shell, a query, a path or a page. Secrets reaching a log.
- **Tests:** would one fail if the change were reverted? A test that passes either way is decoration.
- Rank findings **blocker**, **should-fix**, **note**. Each gets a `path:line` and the wrong behavior, not a vibe. "Nothing found" is a fine review if you say what you looked at.
- **Ask** only when the intent is genuinely unclear and the verdict depends on it. Otherwise review against the most likely intent and say what you assumed.

**Done when** every finding has a location and a consequence, and you've named what you didn't check.
