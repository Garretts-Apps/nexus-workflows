---
description: Add or run one focused test and quote the result
---

# Test

Behavior: $ARGUMENTS

No behavior given? Test what the working diff changed; with no diff, run the suite and work the first failure.

Load the `testing` skill and hold every test to it. This command is the one-test version: one behavior, one test, proven.

- **Pick the narrowest test** that pins the behavior. One good test beats a file of plausible ones.
- **Ask** only when the expected behavior is a product decision the code doesn't settle. Otherwise pin what the code does today and flag anything that looks wrong.

**Done when** the narrowest command that runs the test is quoted with its output, and a fix was shown failing first.
