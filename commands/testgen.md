---
description: Generate a focused unit test file for one module
---

# Test generation

Target: $ARGUMENTS

No target given? The module the working diff changed most, else the most-used module with the thinnest tests. Say which.

Generated tests are only worth keeping if they'd catch a real regression. A file of assertions that restate the implementation is a liability with good coverage numbers.

- **Read the module and its callers.** Test the contract callers depend on, not private helpers.
- Cover the edges the module actually handles: empty, boundary, invalid, error paths. Skip permutations that exercise the same branch.
- **Each test should fail if the behavior it names broke.** If you can't say what would make it fail, delete it.
- Match the runner, file layout and fixtures beside it.
- Fixing a bug? Show the test failing before the fix.
- **Ask** only if the intended behavior conflicts with what the code does.

**Done when** the narrowest command that runs the new file is quoted with its output, and each test's name says what it protects.
