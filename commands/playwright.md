---
description: Add a focused end-to-end browser test
---

# Playwright test

Flow: $ARGUMENTS

No flow given? The path the working diff changed; with no diff, the main path a new person takes. Say which.

End-to-end tests are the slowest and flakiest you own. Each one has to earn its place by covering something only a real browser can.

- **Follow the project's layout,** fixtures and helpers. Find an existing test and copy its shape.
- **Locate by role, label and test id,** the way a person would find things. CSS paths break on the first redesign.
- **Wait for state, never for time.** Web-first assertions that retry; no fixed sleeps. A test that needs a sleep is telling you the app has no observable ready state.
- One happy path and the one failure path that matters most. Leave the permutations to unit tests.
- Own your data: create what the test needs, don't depend on what another test left behind.
- Run it a few times in a row before calling it stable.
- **Ask** only if the flow needs credentials or external services you don't have.

**Done when** the run command and its output are quoted, and the test passed on repeat runs.
