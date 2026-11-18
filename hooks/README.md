# Hook examples (opt-in)

Nothing here runs until you wire it into your harness's settings. buildwithnexus reads hooks from `~/.buildwithnexus/settings.json` or a trusted project's `.buildwithnexus/settings.json`; the `.claude/` layout reads `.claude/settings.json`. Both take the matcher names below (`Bash`, `Write`, `Edit`), and bwn maps them onto its own tools.

## Setup

1. Copy every `*.py` from `scripts/` into `~/.buildwithnexus/hooks/` (or a path you control).
2. Merge `settings.example.json` into your settings `hooks` object. Replace `${KIT_ROOT}/scripts` in each `command` with the directory you copied the scripts to. Nothing expands `KIT_ROOT` for you; it is a placeholder, not a promise.
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

`python3 scripts/check_kit.py` runs `tests/test_hooks.py`, which feeds each guard the JSON a harness would. To poke one by hand:

```bash
echo '{"tool_input":{"command":"git push -f origin main"}}' | python3 scripts/guard_shell.py; echo exit:$?
# expect: exit:2
```

Exit 2 and a reason on stderr means blocked.