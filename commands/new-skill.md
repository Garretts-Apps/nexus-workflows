---
description: Scaffold a skill folder with frontmatter and when-to-use rules
---

# New skill

Name: $ARGUMENTS

No name given? Ask for one, with a suggestion based on the knowledge the conversation keeps re-explaining. This is the one place a bare command can't guess.

A skill is knowledge the agent loads when it needs it. The description decides whether it ever gets loaded, so write that line last and best.

- **`<name>/SKILL.md`** with `name` matching the folder and a `description` that says when to use it, not what it is.
- **Use when** and **Done when** sections. In between, what an expert knows that a competent person doesn't.
- Short enough to read in one sitting. Longer reference material goes in `references/`, scripts in `scripts/`, and only if they're needed.
- No employer, customer or product names in examples.
- Don't register it anywhere outside this tree unless asked.

**Done when** the skill folder exists, its frontmatter is complete, and the description would make you load it at the right moment.
