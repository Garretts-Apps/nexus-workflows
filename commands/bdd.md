---
description: Turn acceptance criteria into Gherkin and step stubs
---

# BDD scenario

Story: $ARGUMENTS

No story given? Take the acceptance criteria from the branch's spec, issue reference or PR text. If none exists anywhere, write the one scenario the working diff implies and label it inferred.

A scenario is a promise in the business's words. If a product owner can't read it, it's a unit test wearing a costume.

- **One behavior per scenario.** Given sets the world, When is one action, Then is something observable. No UI clicks in the steps unless the click is the behavior.
- Include the unhappy path that matters most. Most bugs live there, not in the scenario everyone wrote first.
- **Concrete examples beat abstractions:** "a cart with 3 items totaling 40 dollars" says more than "a valid cart". Use scenario outlines when the examples differ only in data.
- Reuse existing step phrasing so steps stay shared; new wording for an old step is how suites rot.
- Match the project's framework and tags. Stub new steps; leave production code alone unless asked.
- **Ask** only when the expected outcome is a product decision the criteria don't settle.

**Done when** the feature file parses with the project's runner and each new step either binds or fails with a clear pending message.
