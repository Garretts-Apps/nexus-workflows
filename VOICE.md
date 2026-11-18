# Voice

How the kit talks. `scripts/check_kit.py` enforces the parts a script can check.

## Tone

Cheeky and dry. Say the thing, then stop. A joke gets one clause, never a paragraph, and never in a step the agent has to follow. Instructions stay literal: the agent can't tell a wink from an order.

- Short sentences. Verbs first in steps.
- Name the failure you are preventing ("pasted a log nobody ran").
- No cheerleading, no emoji, no exclamation marks.
- Admit limits plainly: "Not rehearsed: ..." beats a confident guess.

## How a command reads

Like the most experienced person on the team, talking to a peer they trust. A command carries judgment, not a script.

- **Say what matters and why.** The traps, the edge cases, the thing people learn the second time. The agent picks the order.
- **Few numbered steps.** Numbers are for order that actually matters (reproduce before you fix). Everything else is a bullet or a sentence.
- **No checkbox theater.** If a rule would make a senior engineer sigh, cut it.
- **Work with no arguments.** `/test` alone is a full request. Find the scope in the repo: the working diff, then the branch against main, then the last commit, then failing tests. Say which one you picked in one line and get on with it.
- **Ask only for what the repo can't tell you.** Intent, trade-offs between options the maintainer would care about, and anything irreversible or outward-facing (deleting, pushing, publishing, spending). Never ask for a fact you could read, run or grep. One question, with a recommended answer, beats five.
- **End with `Done when`.** One line naming the evidence that ends the job. That part is not optional.
- **Leave room.** "Prefer", "usually" and "unless" are allowed when they are true. "Always" is for things that are always true.

## Words we use

Taken from the maintainer's own projects and requests. Prefer these to the generic alternatives.

| Say | Not | Where it comes from |
| --- | --- | --- |
| harness | runtime, host, platform | the maintainer's name for the thing that runs the agent |
| kit | library, collection, pack | this repo |
| command | prompt, recipe | `commands/` |
| skill | playbook, guide | `skills/` |
| helper | subagent, sub-agent | `agents/` |
| guard | policy, rule engine | the hook scripts |
| rehearse | dry-run, smoke-test | run a block in a clean cell before handing it over |
| cell | sandbox, test environment | a clean machine or container for one rehearsal |
| deliverable | output, artifact | "what they will have, on which machine" |
| evidence | proof, validation | quoted command and output |
| the maintainer | the user, the human | whoever owns the repo |
| BUILD, PLAN, BRAINSTORM | modes, phases | the three ways of working |
| deslop | clean up AI output | `/deslop` |
| entropy | tech debt | `/entropy` |
| grill | interrogate, stress-test | `/grill` |
| handoff | summary, recap | `/handoff` |
| CI is green | checks pass | how merges are gated |
| merge to main | ship it | the last step |

## Words we don't use

Marketing words and other projects' vocabulary. The check fails on these (see `BANNED` in `scripts/check_kit.py`): awesome, superpower, supercharge, unleash, seamless, leverage, robust, curated, battle-tested, best practices, game-changer, cutting-edge, powerful, blazing, revolutionize, elevate, empower, delve, comprehensive, magic, agentic, vendor-neutral.

The kit never names another tool, project or company as a reference point. Folder conventions are given by path (`.claude/commands/`), not by product.
