---
description: Add tests for uncovered lines from a coverage report
---

# Coverage gaps

Report: $ARGUMENTS

No report given? Find the one the project already produces; if none exists, run the suite with the project's coverage tool and say which command you used.

Load the `testing` skill. Coverage tells you what never ran, not what was checked: treat it as a map of where bugs can hide, not a score.

- **Rank gaps by risk,** not by count: error handling, money and dates, auth, parsing, branches that guard data loss. A missed `else` in a parser beats a hundred missed getters.
- Skip generated code, trivial accessors and code about to be deleted. Say what you skipped.
- **An unreachable gap is a finding:** dead code is cheaper to delete than to test.
- **Ask** only if the right behavior for an uncovered branch isn't clear from the code.

**Done when** before and after coverage for the touched files are quoted, and each new test names the behavior it protects.
