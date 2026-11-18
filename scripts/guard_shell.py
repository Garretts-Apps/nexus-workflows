#!/usr/bin/env python3
"""PreToolUse guard for risky shell commands. Reads hook JSON from stdin. Exit 2 to block."""
import json
import re
import shlex
import sys


def command_from(payload):
    ti = payload.get("tool_input") or {}
    return (ti.get("command") or "").strip()


def deny(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    cmd = command_from(payload)
    if not cmd:
        sys.exit(0)
    lower = cmd.lower()
    risky = [
        # The target must be the root, home, or a drive itself: rm -rf /tmp/build is fine.
        (r"\brm\s+(-[^\s]*\s+)*-[^\s]*r[^\s]*\s+(/|~/?|\$home/?|\$\{home\}/?|[a-z]:\\?)\*?(\s|$|[;&|])", "recursive delete of root or home"),
        (r"\bmkfs\b", "filesystem format"),
        (r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;", "fork bomb pattern"),
        (r">\s*/dev/[sh]d[a-z]", "raw disk write"),
        (r"\bcurl\b[^\n]*\|\s*(ba)?sh\b", "pipe download into shell"),
        (r"\bwget\b[^\n]*\|\s*(ba)?sh\b", "pipe download into shell"),
        # Only as a command, so grep reboot logs passes.
        (r"(^|[;&|(]\s*)(sudo\s+)?shutdown\b", "shutdown command"),
        (r"(^|[;&|(]\s*)(sudo\s+)?reboot\b", "reboot command"),
    ]
    for pat, label in risky:
        if re.search(pat, lower, re.I):
            deny(f"blocked shell: {label}")
    for segment in re.split(r"&&|\|\||[;|\n]", lower):
        if not re.search(r"\bgit\s+push\b", segment):
            continue
        forced = re.search(r"\s(--force(?!-with-lease)\b|-[a-z]*f[a-z]*\b|\+\S)", segment)
        if forced and re.search(r"\b(main|master)\b", segment):
            deny("blocked shell: force push to default branch")
    for segment in re.split(r"&&|\|\||[;|\n]", lower):
        # Only where git is the command, so `echo git clean -fdx` passes.
        git = re.match(r"\s*(?:sudo\s+)?git(?:\s+-c\s+\S+)*\s+(\S+)(.*)", segment)
        if not git:
            continue
        sub, rest = git.group(1), git.group(2)
        if sub == "reset" and re.search(r"(^|\s)--hard\b", rest):
            deny("blocked shell: git reset --hard throws away uncommitted work; git stash first, or ask")
        clean = re.match(r"(.*)", rest) if sub == "clean" else None
        if clean:
            flags = clean.group(1)
            dry = re.search(r"\s(-[a-z]*n[a-z]*|--dry-run)\b", flags)
            force = re.search(r"\s(-[a-z]*f[a-z]*|--force)\b", flags)
            if force and not dry:
                deny("blocked shell: git clean -f deletes untracked files for good; run git clean -n first, or ask")
    if re.search(r"\bformat\s+[a-z]:", lower):
        deny("blocked shell: format drive")
    if re.search(r"\bdel\s+/[fq]\s+", lower) or re.search(r"\brd\s+/s\b", lower):
        if re.search(r"[c-z]:\\", lower, re.I) or "\\windows" in lower:
            deny("blocked shell: destructive Windows tree delete")
    try:
        parts = shlex.split(cmd)
    except ValueError:
        parts = cmd.split()
    if parts and parts[0] in ("rm", "unlink") and "-r" in "".join(parts):
        if any(p in ("/", "~", "..") for p in parts):
            deny("blocked shell: broad recursive delete")
    sys.exit(0)


if __name__ == "__main__":
    main()