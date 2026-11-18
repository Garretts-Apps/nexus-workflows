# nexus-workflows

Portable Markdown **commands**, **skills**, **agents**, optional **hook scripts**, and **CI workflow examples** for coding agents. Nothing here assumes one vendor runtime.

## Canonical layout

| Path | Format |
| --- | --- |
| `commands/` | One file per slash command: `<name>.md` with optional YAML frontmatter |
| `skills/` | `<name>/SKILL.md` (Agent Skills shape) or flat skill bodies |
| `agents/` | `<name>.md` helper definitions (`name`, `description`, `tools`, `read_only`) |
| `scripts/` | Python helpers (stdlib only; hooks and scanners) |
| `hooks/settings.example.json` | Example hook wiring; paths are placeholders you replace |
| `workflows-examples/` | Optional GitHub Actions samples |
| `AGENTS.md` | Repository-level instructions many agents read automatically |

## Install

Copy only what you need. Names must match on disk (e.g. `commit.md` → `/commit`).

### buildwithnexus (bwn)

Many of these commands ship **built-in** in current bwn releases. To override or extend, copy into `~/.buildwithnexus/commands/`, `~/.buildwithnexus/skills/`, or `~/.buildwithnexus/agents/`. Hook scripts: `~/.buildwithnexus/hooks/` plus `hooks` in `~/.buildwithnexus/settings.json`.

### Claude Code

Copy into the project or home tree: `.claude/commands/`, `.claude/skills/`, `.claude/agents/`, and `.claude/scripts/`. Merge `hooks/settings.example.json` into `.claude/settings.json` and point commands at your script directory.

### Cursor

Project rules: merge `AGENTS.md` at the repo root (or `.cursor/rules` if you split it). Commands: `.cursor/commands/` if your setup supports markdown commands, else keep under `.claude/commands/` (Cursor reads both in many setups). Skills: `.cursor/skills/` or `.agents/skills/` using the same `SKILL.md` folders.

### Codex / generic AGENTS.md hosts

Use root `AGENTS.md`. Place skills under `.agents/skills/<name>/SKILL.md`. Invoke commands by pasting the markdown body or wiring your runner's slash-command folder to `commands/`.

### Other CLIs

Map `commands/` → the tool's slash-command directory, `skills/` → the tool's skill directory, `agents/` → subagent or helper directory, `scripts/` → a path on `PATH` or referenced by hook JSON.

## Scanners

From the kit root:

```bash
python3 scripts/scan_slop.py --report .
python3 scripts/scan_secrets.py --report .
python3 scripts/measure_entropy.py --report .
```
