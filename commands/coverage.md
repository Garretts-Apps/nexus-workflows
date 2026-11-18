---
description: Add tests for uncovered lines from a coverage report
---

# Coverage gaps

Report: $ARGUMENTS

No report given? Find the one the project already produces; if none exists, run the suite with the project's coverage tool and say which command you used.

Coverage tells you what never ran. It says nothing about what was checked. Treat it as a map of where bugs can hide, not a score.

- **Rank gaps by risk,** not by count: error handling, money and dates, auth, parsing, branches that guard data loss. A missed `else` in a parser beats a hundred missed getters.
- **Every new test asserts something** that would fail if the behavior regressed. Executing a line without checking it is coverage theater.
- Skip generated code, trivial accessors and code that is about to be deleted. Say what you skipped.
- If a gap is unreachable, that's a finding: dead code is cheaper to delete than to test.
- **Ask** only if the right behavior for an uncovered branch isn't clear from the code.

**Done when** before and after coverage for the touched files are quoted, and each new test names the behavior it protects.
