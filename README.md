# nexus-workflows

Commands, skills and helpers for a coding agent that would otherwise say "done" without running anything.

It is Markdown and standard-library Python. No install step, no dependencies, no account. Copy the files you want into your harness and delete the rest; nothing here will notice.

| Path | What it is |
| --- | --- |
| `commands/` | 47 slash commands. `commit.md` is `/commit`. The body is the prompt; `description` is what the popup shows. |
| `skills/` | 8 skills, one `<name>/SKILL.md` each, with `name` and `description` frontmatter. |
| `agents/` | 4 read-only helpers: `reviewer`, `security-check`, `pipeline-reviewer`, `debugger`. |
| `scripts/` | Guards and scanners. Python 3, stdlib only, Linux, macOS and Windows. |
| `hooks/` | Example wiring for the guards. Off until you turn it on. |
| `workflows-examples/` | GitHub Actions to copy: secret scan, dependency audit, CodeQL. |
| `AGENTS.md` | House rules for any agent working in a repo that uses the kit. |
| `INDEX.md` | Every command, skill, helper and script on one page, generated so it can't go stale. |
| `VOICE.md` | How the kit talks, and the words it won't use. |

## What it insists on

- **Evidence or it didn't happen.** Commands that change behavior end with a command and its quoted output. `verify-before-done` is the skill for agents that would rather not.
- **Reproduce first.** `/debug` names the first wrong line before anyone edits it.
- **Small commits.** One concern each, conventional subject, no amend or force-push unless asked.
- **Read-only by default.** Helpers review; they don't fix. The parent agent decides.
- **Admit what wasn't run.** "Not rehearsed" is a fine sentence. A confident guess is not.

## Install

`scripts/install_kit.py` copies the kit into the folders your harness reads. Look before it leaps:

```bash
python3 scripts/install_kit.py --layout bwn --dry-run
# expect: dry run:
```

Drop `--dry-run` to copy. `--layout claude --into <project>` or `--layout agents --into <project>` for the other layouts, `--only skills` (or `commands`, `agents`, `scripts`) for part of the kit. It never deletes, and a file you've edited is skipped and reported, not overwritten, unless you pass `--force`. Rerunning it is safe; unchanged files print `same`.

Or copy by hand. Names must match on disk.

| Kit folder | buildwithnexus | `.claude/` layout | `.agents/` layout |
| --- | --- | --- | --- |
| `commands/` | `~/.buildwithnexus/commands/` | `.claude/commands/` | your runner's command folder |
| `skills/` | `~/.buildwithnexus/skills/` | `.claude/skills/` | `.agents/skills/` |
| `agents/` | `~/.buildwithnexus/agents/` | `.claude/agents/` | your runner's helper folder |
| `scripts/` | `~/.buildwithnexus/hooks/` | `.claude/scripts/` | anywhere on `PATH` |
| `AGENTS.md` | repo root | repo root | repo root |

A project folder (`.buildwithnexus/`, `.claude/`) works too, once the harness trusts the project.

buildwithnexus already bundles `/test`, `/handoff`, `/changelog`, `/design-pass` and `/deslop`, plus the `distinctive-design` and `deslop` skills (main, after 0.21.0). A file of the same name in your commands folder replaces the bundled one. bwn's own `/commit`, `/review`, `/pr` and `/debug` answer before any file, so the kit's versions of those run headless only: `bwn run '/commit'`.

Hooks: see `hooks/README.md`.

## Scanners

From the kit root, or point them at any tree:

- `python3 scripts/scan_slop.py --report .` for invisible Unicode, smart quotes and stray dashes. `--ci` exits 1 only on characters you can't see.
- `python3 scripts/scan_secrets.py --report .` for key shapes and labeled secrets.
- `python3 scripts/measure_entropy.py --report .` for big files, repeated blocks and churn.
- `python3 scripts/lint_blocks.py <file.md>` for command blocks someone will paste: each must end with `# expect: <text>`. `/rehearse` takes it from there.

The scanners report and exit 0. A clean tree prints nothing, which is the most enthusiasm they've got.

## Checking the kit

```bash
python3 scripts/check_kit.py
# expect: kit ok
```

Frontmatter, voice, every backticked path and slash command resolving, every script compiling, and the guard tests in `tests/`. CI runs it on Linux, macOS and Windows. It prints `kit ok` or a list, which is the only mood it has.
