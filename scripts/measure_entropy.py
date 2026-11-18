#!/usr/bin/env python3
"""Rank simple entropy hotspots in a source tree. Report only; stdlib; Windows-safe."""
import argparse
import hashlib
import subprocess
import sys
from collections import Counter
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
    "out",
    ".turbo",
    ".cache",
}
TEXT_SUFFIX = {
    ".py",
    ".rs",
    ".go",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".cs",
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".css",
    ".scss",
    ".html",
    ".sh",
}
LINE_BLOCK = 5
MIN_BLOCK_LEN = 40
LARGE_FILE = 400
# Copies here are on purpose (fixtures mirror real files) or generated
# (data dumps), so they are not duplication worth paying down.
DUP_SKIP_DIRS = {"fixtures", "test-fixtures", "__fixtures__", "testdata", "snapshots", "__snapshots__"}
DUP_SKIP_SUFFIX = {".json"}
DUP_SHOWN = 25  # the longest copies; the rest are counted, not listed


def iter_sources(root: Path):
    root = root.resolve()
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIX:
            continue
        if looks_binary(path):
            continue
        yield path


def looks_binary(path: Path) -> bool:
    try:
        chunk = path.read_bytes()[:8192]
    except OSError:
        return True
    return b"\0" in chunk


def read_lines(path: Path):
    try:
        return path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []


def large_files(root: Path):
    for path in iter_sources(root):
        lines = read_lines(path)
        if len(lines) >= LARGE_FILE:
            rel = path.relative_to(root).as_posix()
            yield ("LARGE_FILE", rel, len(lines))


def duplicate_blocks(root: Path):
    """One finding per copied run, not per matching window.

    A 20-line copy matches 16 overlapping 5-line windows; they are joined
    into one run with both line ranges, and runs are ranked by length.
    """
    seen = {}  # window digest -> (file, first line) where it first appeared
    runs = []
    for path in iter_sources(root):
        if path.suffix.lower() in DUP_SKIP_SUFFIX or DUP_SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        lines = read_lines(path)
        rel = path.relative_to(root).as_posix()
        hits = []  # (line here, other file, line there), 1-based
        for i in range(len(lines) - LINE_BLOCK + 1):
            block = [ln.strip() for ln in lines[i : i + LINE_BLOCK]]
            text = "\n".join(block)
            if len(text) < MIN_BLOCK_LEN:
                continue
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
            first = seen.get(digest)
            if first and first[0] != rel:
                hits.append((i + 1, first[0], first[1]))
            elif not first:
                seen[digest] = (rel, i + 1)
        for here, other, there in hits:
            last = runs[-1] if runs else None
            if last and last[0] == rel and last[2] == other and here == last[1] + last[4] and there == last[3] + last[4]:
                last[4] += 1
            else:
                runs.append([rel, here, other, there, 1])
    runs.sort(key=lambda r: (-r[4], r[0], r[1]))
    findings = []
    for rel, here, other, there, windows in runs[:DUP_SHOWN]:
        size = windows + LINE_BLOCK - 1
        findings.append(("DUP_BLOCK", rel, f"{rel}:{here}-{here + size - 1} = {other}:{there}-{there + size - 1} ({size} lines)"))
    if len(runs) > DUP_SHOWN:
        findings.append(("DUP_BLOCK", "...", f"{len(runs) - DUP_SHOWN} shorter copies not listed"))
    return findings


def git_churn(root: Path, limit: int = 15):
    try:
        out = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "log",
                "--since=90.days",
                "--pretty=format:",
                "--name-only",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return []
    if out.returncode != 0:
        return []
    counts = Counter(p for p in out.stdout.splitlines() if p.strip())
    ranked = counts.most_common(limit)
    return [("GIT_CHURN", path, count) for path, count in ranked]


def scan(root: Path):
    findings = []
    findings.extend(large_files(root))
    findings.extend(duplicate_blocks(root))
    findings.extend(git_churn(root))
    return findings


def main():
    parser = argparse.ArgumentParser(description="Report entropy hotspots.")
    parser.add_argument("paths", nargs="*", type=Path, default=[Path.cwd()])
    parser.add_argument("--report", action="store_true", help="print and exit 0 (the default; kept for scripts)")
    args = parser.parse_args()
    all_findings = []
    for path in args.paths:
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            return 2
        path = path.resolve()
        base = path if path.is_dir() else path.parent
        all_findings.extend(scan(base))
    def sort_key(item):
        kind, where, detail = item
        if kind == "LARGE_FILE":
            return (0, -int(detail), where)
        if kind == "GIT_CHURN":
            return (1, -int(detail), where)
        return (2, 0, "")  # already ranked longest first

    for kind, where, detail in sorted(all_findings, key=sort_key):
        print(f"{kind}\t{where}\t{detail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())