# Agent instructions

House rules for any agent working in a repo that uses this kit. Short on purpose: the commands and skills carry the detail.

## How to work

- **Read before you edit.** The repo's own style, tests and tooling win over your preferences, and over this kit's.
- **Find the scope yourself.** The working diff, then the branch against main, then the last commit. Say which one you picked.
- **Ask only what the repo can't answer:** intent, a trade-off the maintainer would care about, or anything irreversible or outward-facing (deleting, pushing, publishing, spending). One question, with a recommended answer. Never ask for a fact you could read or run.
- **Evidence or it didn't happen.** "Done", "fixed" and "passing" come with the command and its quoted output. Say what you didn't run.
- **Small commits,** one reason each, with a subject that says what changed. No amend, force-push or skipped hooks unless asked.
- **No secrets in the tree,** in logs, or in anything you paste. A key that reached a remote gets rotated, not just deleted.

## Which skill, when

| When | Load |
| --- | --- |
| Writing or judging tests | `testing` |
| A function whose "always" and "never" matter more than its examples | `lean` |
| About to say done, fixed or passing | `verify-before-done` |
| Planning or building a feature | `vertical-slicing` |
| Handing the maintainer commands to run on their machine | `rehearse` |
| Touching input handling, auth, secrets, shell or queries | `security-review` |
| Changing a public interface | `api-design` |
| Designing or restyling a screen | `distinctive-design` |
| After a lot of generated code or prose | `deslop` |
| Splitting work across helpers | `agent-orchestration` |

## Helpers

Hand narrow, read-only jobs to `reviewer` (defects in a diff), `security-check` (untrusted input to dangerous sinks), `pipeline-reviewer` (CI/CD definitions) and `debugger` (reproduce and name the cause). They all return the same report: scope, a severity table with `path:line` and evidence, and what wasn't checked. Check a finding before you repeat it.

## In this repo

Working on the kit itself:

- `python3 scripts/check_kit.py` before every commit. It prints `kit ok` or a list.
- `python3 scripts/build_index.py` after adding, removing or renaming a command, skill or helper. A stale `INDEX.md` fails the check.
- New commands and skills follow `VOICE.md`. The check enforces the shape; the voice is on you.
