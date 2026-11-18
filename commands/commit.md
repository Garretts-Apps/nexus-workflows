---
description: Review the diff, skip secrets, run a fast check, and create one commit
---

# Commit

Scope: $ARGUMENTS

No scope given? Everything changed, split into as many commits as it has reasons.

A commit is one reason to change. If the subject needs "and", it's two commits.

- **Read the whole staged diff** and stage paths on purpose. Debug prints, generated noise, unrelated lockfile churn and anything that looks like a key stay out. A key that gets committed is a key that gets rotated.
- **Subject:** what changes, imperative, short. **Body:** why, plus whatever the next reader would otherwise have to ask. The diff already says how.
- **Run the fastest check that would catch this change breaking** and quote it. A commit that "should be fine" is a guess with a hash.
- No amend, no force-push, no skipping hooks unless asked. A failing hook is information, not an obstacle.
- **Ask before** committing something that looks like a secret or a large binary, or splitting work the maintainer may want as one commit. Don't ask what the message should say; write it.

**Done when** `git log -1 --stat` shows the commit with only the intended files.
