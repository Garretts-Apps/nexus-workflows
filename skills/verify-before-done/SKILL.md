---
name: verify-before-done
description: Use before saying anything is done, fixed or passing: run the narrowest proof and quote it
---

# Verify before done

**Use when** you're about to say done, fixed, passing, working or ready. Also when judging someone else's "done".

"Done" is a claim about the world. Evidence or it didn't happen.

- **Say what done means** in one line, in terms someone can observe: a test passes, a page renders, a command prints the version.
- **Run the narrowest thing that proves it,** and quote the command and its output. Not a summary of the output. The output.
- **A bug fix shows red then green:** the reproduction failing before, passing after. Without the red, you don't know the test tests anything.
- **Say what you didn't run:** the full suite, other platforms, the slow integration job. Unrun isn't failed, but it isn't passed either.
- **If the output disagrees with the claim, the output wins.** Fix it or report it. Don't explain it away.
- Truncated logs say they're truncated.

**Done when** the claim, the command, its quoted output and the list of what wasn't run are all in the reply.
