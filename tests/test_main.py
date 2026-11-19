import tempfile
import unittest
from pathlib import Path
from main import inspect_text, scan

class LicenseHeaderTests(unittest.TestCase):
    def test_finds_spdx_header(self):
        result = inspect_text("# SPDX-License-Identifier: MIT\nprint('ok')")
        self.assertTrue(result["found"])
        self.assertEqual(result["identifier"], "MIT")
    def test_checks_only_configured_lines(self):
        self.assertFalse(inspect_text("a\nb\nc\n# SPDX-License-Identifier: MIT", 2)["found"])
    def test_scan_reports_missing_header(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "app.py"
            path.write_text("print('hello')", encoding="utf-8")
            self.assertEqual(scan(Path(folder)), [{"path": str(path), "issue": "missing-spdx-header"}])

if __name__ == "__main__":
    unittest.main()
