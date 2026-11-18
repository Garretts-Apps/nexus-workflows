---
description: Draft a pull request title and body from the branch diff
---

# Pull request draft

Context: $ARGUMENTS

No context given? The current branch against its merge base.

A PR description is for the reviewer who has ten minutes and no context. Spend them well.

- **Title:** what changes, in the reader's terms. Not the ticket number, not the branch name.
- **Why first,** then what. The diff already says how.
- **What to look at:** the risky part, the part you're unsure about, anything that looks wrong but is deliberate.
- **How it was verified:** commands and results. "Tested locally" is not a result.
- Breaking changes and follow-ups called out, not buried.
- Use the repo's PR template if there is one, as a layout.
- Pushing and opening the PR are outward-facing: **ask** unless the maintainer already said to.

**Done when** the title and body are drafted and every claim of testing has a command next to it.
