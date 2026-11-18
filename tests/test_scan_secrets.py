"""scan_secrets.py: literal secrets are caught; code that merely says "secret" is not."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "scan_secrets.py"
# Built from parts so this file does not look like it holds a key.
KEY = "sk-" + "q7Rm2vXc9LpT4wZb8NdK3hJs"
PW = "pass" + "word"
VALUE = "h4" * 6


def scan(files):
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in files.items():
            target = Path(tmp, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        out = subprocess.run([sys.executable, str(SCRIPT), "--report", tmp],
                             capture_output=True, text=True, check=True).stdout
    return out.splitlines()


class ScanSecrets(unittest.TestCase):
    def test_literals_are_caught(self):
        got = scan({
            "app.py": f'{PW} = "{VALUE}"\n',
            "conf.json": '{"apiKey": "' + VALUE + '"}\n',
            ".env": f"DB_{PW.upper()}={VALUE}\n",
            "k.ts": f"const k = '{KEY}';\n",
        })
        self.assertEqual(got, [".env:1:labeled_secret", "app.py:1:labeled_secret",
                               "conf.json:1:labeled_secret", "k.ts:1:api_key_shape"])

    def test_code_and_placeholders_are_not(self):
        got = scan({
            "auth.rs": "pub client_secret: Option<String>,\nlet secret = dir.join(\"keys\");\n"
                       "access_token: String::new(),\n",
            "ci.yml": "github-token: token-for-the-mock\napi_key: ${{ env.KEY }}\n",
            "doc.md": 'Set api_key = "your-key-here" first.\n',
            "oauth.rs": 'token_endpoint: "https://login.example/token",\n',
        })
        self.assertEqual(got, [])

    def test_test_files_come_last_and_say_so(self):
        line = f'token = "{VALUE}"\n'
        got = scan({"src/a.py": line, "tests/test_a.py": line})
        self.assertEqual(got, ["src/a.py:1:labeled_secret", "tests/test_a.py:1:labeled_secret:test"])


if __name__ == "__main__":
    unittest.main()
