---
description: Scaffold a slash command markdown file
---

# New command

Name: $ARGUMENTS

No name given? Ask for one, with a suggestion based on what the maintainer keeps typing by hand. This is the one place a bare command can't guess.

Write it the way `VOICE.md` says a command reads: judgment, not a script.

- **One outcome.** The `description` says it in a line the popup can show.
- **Works with no arguments:** say where it finds its scope in the repo when nothing is typed.
- **What matters:** the things an experienced person watches for, as bullets. Number only what must happen in order.
- **When to ask:** only what the repo can't answer, with a recommended answer.
- **End with `Done when`** and the evidence.
- No secrets, no host-specific URLs, no hooks unless asked. `$ARGUMENTS` for free text; don't use `$1`-style placeholders in prose.

**Done when** the file exists and `python3 scripts/check_kit.py` passes with it in place (or the project's equivalent check does).
