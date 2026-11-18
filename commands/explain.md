---
description: Explain behavior in plain language with a fixed writing shape
---

# Explain

Subject: $ARGUMENTS

No subject given? Explain whatever the working diff changes; with no diff, how a request travels through the main entry point.

Read the code before you write a word. An explanation of what the code probably does is fiction.

Shape the reply like this:

1. **What it is** in one sentence a newcomer can follow.
2. **How it runs,** in execution order, naming the files and functions as you go.
3. **What can go wrong:** the two or three failure modes that actually happen, not every theoretical one.
4. **Where to look next:** paths and commands, no hand-waving.

- Match depth to the question. "What does this do?" doesn't need the architecture tour.
- Say where you're unsure and what would settle it.
- Read-only. No edits unless asked.

**Done when** every claim in the explanation points at a file, function or command.
