---
description: Generate a focused unit test file for one module
---

# Test generation

Target: $ARGUMENTS

No target given? The module the working diff changed most, else the most-used module with the thinnest tests. Say which.

Load the `testing` skill. This command is the whole-module version, and generated tests are where its "never be" list matters most: a file of assertions that restate the implementation is a liability with good coverage numbers.

- **Read the module and its callers** first, then list the behaviors worth pinning before writing any.
- **Cut** every test whose failure you can't describe in one line.
- **Ask** only if the intended behavior conflicts with what the code does.

**Done when** the narrowest command that runs the new file is quoted with its output, and each test's name says what it protects.
