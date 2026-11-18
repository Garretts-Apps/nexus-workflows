---
description: Walk a UI flow in a browser and list fixable issues
---

# User journey

Flow: $ARGUMENTS

No flow given? The main path a new person takes: land, sign up or start, do the core thing once. Say which.

Walk it as the person, not as the developer who knows where everything is.

- **Run it locally** or on the URL given, in a real browser, at a phone width and a desktop width. Capture each step.
- Watch for: a dead end, a step with no clear next action, missing labels, errors that blame the user, layout that breaks at small widths, console errors, slow steps.
- **Do it with the keyboard once.** If you can't finish, neither can some of the people using it.
- Rank issues by how many people hit them and how badly. Each issue gets the step, a screenshot and a file hint when you saw one.
- Read-only against anything shared: no real accounts, no production data, no form submits that send email or charge money. **Ask** before any of those.

**Done when** every step has a capture, and every issue has a severity and a screenshot.
