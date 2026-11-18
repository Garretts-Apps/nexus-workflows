# Hook examples (opt-in)

Nothing here runs until you wire it into your agent's settings. bwn and Claude Code both run hooks from their settings files (`~/.buildwithnexus/settings.json` or a trusted project `.buildwithnexus/settings.json`; `.claude/settings.json`), and both accept the Claude Code tool names used in the matchers below.

## Setup

1. Copy every `*.py` from `scripts/` into `~/.buildwithnexus/hooks/` (or a path you control).
2. Merge `settings.example.json` into your settings `hooks` object. Replace `${KIT_ROOT}/scripts` in each `command` with the directory you copied the scripts to; neither bwn nor Claude Code expands `KIT_ROOT`.
3. The example uses `python`. On Linux and macOS, where `python` is often missing, change it to `python3`; on Windows, `python` or `py -3`. Scripts use only the Python standard library.

## What each script does

| Script | Event | Behavior |
| --- | --- | --- |
| `guard_shell.py` | PreToolUse (shell) | Blocks a short list of destructive shell patterns |
| `guard_writes.py` | PreToolUse (write/edit) | Blocks writes outside the session `cwd` |
| `screen_prompt.py` | UserPromptSubmit | Exit 2 when the prompt looks like it contains a credential |
| `strip_invisible.py` | PostToolUse (write/edit) | Removes invisible Unicode from the file just written |

Exit code `2` means deny (PreToolUse / UserPromptSubmit). PostToolUse hooks only add context; `strip_invisible.py` edits the file in place and always exits 0 on success.

## Tests

From the kit root:

```bash
echo '{"tool_input":{"command":"rm -rf /"}}' | python3 scripts/guard_shell.py; echo exit:$?
```

A block returns exit 2.