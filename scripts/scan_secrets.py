#!/usr/bin/env python3
"""Report likely secret patterns in text files. Stdlib only; read-only.

Prints path:line:label, and :test after it for hits in test files and
fixtures, which are listed last.
"""
import argparse
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "target",
    "vendor",
    ".venv",
    "venv",
    "__pycache__",
    "coverage",
    ".next",
}
# Shapes that are a key whatever surrounds them.
PATTERNS = [
    (r"\bsk-[A-Za-z0-9]{20,}\b", "api_key_shape"),
    (r"\bAKIA[0-9A-Z]{16}\b", "aws_access_key"),
    (r"\bghp_[A-Za-z0-9]{20,}\b", "github_token"),
    (r"(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", "private_key"),
]
LABEL = r"\w*(?:password|passwd|api[_-]?key|secret|token)\w*"
# A labeled secret is a literal value, not code: `api_key = "..."` counts,
# `client_secret: Option<String>` and `let secret = dir.join("keys")` do not.
QUOTED = re.compile(r"(?i)\b" + LABEL + r"""["']?\s*[:=]\s*["']([^"'\s]{8,})["']""")
# Config files also hold bare values: API_KEY=abc123... on a line of its own.
BARE = re.compile(r"(?i)^\s*(?:export\s+)?[\"']?" + LABEL + r"""["']?\s*[:=]\s*([^\s"'#$<{\[][^\s"']{7,})\s*$""")
CONFIG_SUFFIX = {".env", ".ini", ".cfg", ".conf", ".properties", ".yaml", ".yml", ".toml"}
PLACEHOLDER = re.compile(r"(?i)^(?:https?://|/|\./|~/)|example|sample|your|xxx|changeme|change_me|dummy|fake|mock|placeholder|redacted|<|\$\{|\$\(|\*\*\*|\.\.\.")
# Fake keys belong in tests; a hit there is listed, but after the real ones.
TEST_DIRS = {"test", "tests", "__tests__", "spec", "fixtures", "test-fixtures", "testdata", "__fixtures__"}
TEST_NAME = re.compile(r"(?i)(^test_|_test\.|\.test\.|\.spec\.|_tests?\.rs$)")


def is_config(path: Path) -> bool:
    return path.suffix.lower() in CONFIG_SUFFIX or path.name.startswith(".env")


def is_test(rel: str) -> bool:
    parts = rel.split("/")
    return bool(TEST_DIRS & set(p.lower() for p in parts[:-1])) or bool(TEST_NAME.search(parts[-1]))


def labeled(line: str, config: bool) -> bool:
    for pattern in (QUOTED, BARE) if config else (QUOTED,):
        match = pattern.search(line)
        if match and not PLACEHOLDER.search(match.group(1)):
            return True
    return False


def iter_files(root: Path):
    root = root.resolve()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        try:
            if b"\0" in path.read_bytes()[:4096]:
                continue
        except OSError:
            continue
        yield path


def scan(root: Path):
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(root).as_posix()
        config, test = is_config(path), is_test(rel)
        for i, line in enumerate(text.splitlines(), 1):
            hits = [label for pat, label in PATTERNS if re.search(pat, line)]
            if not hits and labeled(line, config):
                hits.append("labeled_secret")
            for label in hits:
                findings.append((test, rel, i, label))
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true")
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    roots = args.paths or [Path.cwd()]
    all_f = []
    for root in roots:
        if not root.exists():
            print(f"missing: {root}", file=sys.stderr)
            return 2
        root = root.resolve()
        base = root if root.is_dir() else root.parent
        all_f.extend(scan(base))
    # Real files first; test and fixture hits after, marked so.
    for test, rel, line, label in sorted(all_f):
        print(f"{rel}:{line}:{label}" + (":test" if test else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())