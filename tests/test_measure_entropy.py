"""measure_entropy.py: a copied block is one finding with both ranges, not one per line."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "measure_entropy.py"
BODY = "".join(f"value_{n} = compute_something_long({n}, flag=True)\n" for n in range(20))


def dups(files):
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in files.items():
            target = Path(tmp, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        out = subprocess.run([sys.executable, str(SCRIPT), "--report", tmp],
                             capture_output=True, text=True, check=True).stdout
    return [line.split("\t")[2] for line in out.splitlines() if line.startswith("DUP_BLOCK")]


class DuplicateBlocks(unittest.TestCase):
    def test_one_copy_is_one_finding(self):
        got = dups({"a.py": BODY, "b.py": "import os\n\n" + BODY})
        self.assertEqual(got, ["b.py:3-22 = a.py:1-20 (20 lines)"])

    def test_longest_copy_comes_first(self):
        short = "".join(f"other_{n} = compute_something_long({n}, flag=False)\n" for n in range(6))
        got = dups({"a.py": BODY + short, "b.py": short, "c.py": BODY})
        self.assertEqual(len(got), 2)
        self.assertTrue(got[0].endswith("(20 lines)"), got)

    def test_fixtures_and_data_are_not_duplication(self):
        got = dups({"a.py": BODY, "tests/fixtures/a.py": BODY, "data.json": BODY})
        self.assertEqual(got, [])


if __name__ == "__main__":
    unittest.main()
