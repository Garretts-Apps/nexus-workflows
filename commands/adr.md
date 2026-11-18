---
description: Record one architecture decision in a short ADR file
---

# Architecture decision record

Topic: $ARGUMENTS

No topic given? Look for a decision already made in the working diff or the last few commits that nobody wrote down: a new dependency, a storage choice, a changed boundary. Say which one you picked.

An ADR exists so the person who wants to undo this in a year knows what it cost the first time. Write for them, not for the meeting.

- **Context is the constraint, not the history.** What forced a choice now, and what was true at the time that might stop being true.
- **The decision in one sentence,** in the active voice. "We will" beats "it was decided".
- **Consequences include the bad ones.** What gets harder, what you are now locked into, what to watch for. An ADR with only upsides is a press release.
- **Alternatives get one honest line each:** why not, in terms someone could re-check later.
- Follow the repo's existing ADR folder and numbering. With none, `docs/adr/NNNN-short-title.md`. Superseding an old ADR? Link both ways.
- **Ask** only if the decision itself is still open. Then it's a `/grill`, not an ADR.

**Done when** the file exists, its status says proposed or accepted, and the consequences section has at least one cost.
