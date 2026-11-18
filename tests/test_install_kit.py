"""install_kit.py: dry runs write nothing, reruns are idempotent, your edits survive."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "install_kit.py"


def run(*args):
    out = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
    return out.returncode, out.stdout, out.stderr


def files(root):
    return sorted(p.relative_to(root).as_posix() for p in Path(root).rglob("*") if p.is_file())


class InstallKit(unittest.TestCase):
    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, _ = run("--layout", "claude", "--into", tmp, "--dry-run")
            self.assertEqual(code, 0)
            self.assertIn("dry run:", out)
            self.assertIn("copy", out)
            self.assertEqual(files(tmp), [])

    def test_claude_layout_and_rerun(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(run("--layout", "claude", "--into", tmp)[0], 0)
            got = files(tmp)
            self.assertIn(".claude/commands/test.md", got)
            self.assertIn(".claude/skills/rehearse/SKILL.md", got)
            self.assertIn(".claude/scripts/guard_shell.py", got)
            self.assertNotIn(".claude/scripts/check_kit.py", got)
            _, out, _ = run("--layout", "claude", "--into", tmp)
            self.assertNotIn("copy ", out)
            self.assertIn("same", out)

    def test_bwn_layout_puts_scripts_in_hooks(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, out, _ = run("--layout", "bwn", "--into", tmp, "--only", "scripts")
            self.assertIn("hooks/guard_shell.py", "\n".join(files(tmp)))
            self.assertNotIn("commands/", "\n".join(files(tmp)))

    def test_your_edit_is_kept_unless_forced(self):
        with tempfile.TemporaryDirectory() as tmp:
            run("--layout", "agents", "--into", tmp, "--only", "commands")
            mine = Path(tmp, ".agents", "commands", "test.md")
            mine.write_text("my own /test\n", encoding="utf-8")
            _, out, _ = run("--layout", "agents", "--into", tmp, "--only", "commands")
            self.assertIn("skip", out)
            self.assertEqual(mine.read_text(encoding="utf-8"), "my own /test\n")
            run("--layout", "agents", "--into", tmp, "--only", "commands", "--force")
            self.assertNotEqual(mine.read_text(encoding="utf-8"), "my own /test\n")

    def test_bad_part_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _, err = run("--layout", "claude", "--into", tmp, "--only", "plugins")
            self.assertEqual(code, 2)
            self.assertIn("unknown part", err)


if __name__ == "__main__":
    unittest.main()
