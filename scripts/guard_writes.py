#!/usr/bin/env python3
"""PreToolUse guard: block writes outside the session working tree. Exit 2 to block."""
import json
import os
import sys
from pathlib import Path

BLOCKED = [
    "/etc",
    "/usr",
    "/bin",
    "/sbin",
    "/var",
    "/sys",
    "/proc",
    "/dev",
]
if os.name == "nt":
    BLOCKED.extend(
        [
            r"C:\Windows",
            r"C:\Program Files",
            r"C:\Program Files (x86)",
        ]
    )


# Tools that write files, by the names harnesses use. A payload with some
# other tool_name (a read, a search) is none of this guard's business.
WRITE_TOOLS = {
    "write", "edit", "multiedit", "notebookedit",
    "write_file", "edit_file", "multi_edit", "create_file", "remove_path", "move_path", "create_dir",
}


def is_write(payload):
    name = str(payload.get("tool_name") or "").lower()
    return not name or name in WRITE_TOOLS


def deny(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def resolve_under(cwd: Path, target: Path) -> bool:
    try:
        cwd = cwd.resolve()
        target = target.resolve()
    except OSError:
        return False
    try:
        target.relative_to(cwd)
        return True
    except ValueError:
        return False


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    if not is_write(payload):
        sys.exit(0)
    cwd_s = payload.get("cwd") or os.getcwd()
    cwd = Path(cwd_s)
    ti = payload.get("tool_input") or {}
    fp = ti.get("file_path") or ti.get("path")
    if not fp:
        sys.exit(0)
    path = Path(fp)
    if not path.is_absolute():
        path = cwd / path
    # A system directory is off limits unless the session itself runs inside
    # it (a project under /var/www). Compare whole path components, so
    # /usrlocal is not /usr.
    for prefix in BLOCKED:
        root = Path(prefix)
        if resolve_under(root, path) and not resolve_under(root, cwd):
            deny(f"blocked write outside project tree: {fp}")
    if not resolve_under(cwd, path):
        deny(f"blocked write outside cwd: {fp}")
    sys.exit(0)


if __name__ == "__main__":
    main()