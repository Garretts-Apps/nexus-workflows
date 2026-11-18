"""lint_blocks.py: the expect rule and the bare-exit rule."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "lint_blocks.py"
TICKS = "`" * 3


def run(markdown):
    with tempfile.TemporaryDirectory() as tmp:
        doc = Path(tmp) / "doc.md"
        doc.write_text(markdown, encoding="utf-8")
        out = subprocess.run([sys.executable, str(SCRIPT), str(doc)], capture_output=True, text=True)
        return out.returncode, out.stdout


class LintBlocks(unittest.TestCase):
    def test_good_block_passes(self):
        code, out = run(f"{TICKS}bash\nbwn version\n# expect: buildwithnexus\n{TICKS}\n")
        self.assertEqual((code, out), (0, ""))

    def test_expect_exit_may_follow(self):
        code, _ = run(f"{TICKS}powershell\nfoo\n# expect: not found\n# expect-exit: any\n{TICKS}\n")
        self.assertEqual(code, 0)

    def test_missing_expect_fails(self):
        code, out = run(f"{TICKS}sh\necho hi\n{TICKS}\n")
        self.assertEqual(code, 1)
        self.assertIn("does not end with", out)

    def test_empty_expect_fails(self):
        code, out = run(f"{TICKS}bash\necho hi\n# expect:\n{TICKS}\n")
        self.assertEqual(code, 1)
        self.assertIn("no text", out)

    def test_bare_exit_fails(self):
        code, out = run(f"{TICKS}bash\necho hi\nexit 1\n# expect: hi\n{TICKS}\n")
        self.assertEqual(code, 1)
        self.assertIn("bare 'exit'", out)

    def test_non_shell_blocks_are_ignored(self):
        code, _ = run(f"{TICKS}json\n{{}}\n{TICKS}\n{TICKS}\nplain\n{TICKS}\n")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
