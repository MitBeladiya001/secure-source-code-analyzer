import unittest
import os
from datetime import datetime
from core import report

class TestReport(unittest.TestCase):
    def setUp(self):
        self.results = {
            "malicious": ["Suspicious eval in file.py"],
            "insecure": ["Hardcoded secret in config.py"],
            "dependencies": ["Vulnerable package found"]
        }
        self.config = {
            "reporting": {
                "output_format": "json",
                "save_path": "./test_reports"
            }
        }

    def test_generate_report(self):
        # Generate a report and confirm it exists
        report.generate_report(self.results, self.config)
        reports = os.listdir(self.config["reporting"]["save_path"])
        self.assertGreater(len(reports), 0)

    def tearDown(self):
        # Clean up generated reports after testing
        reports = os.listdir(self.config["reporting"]["save_path"])
        for file in reports:
            os.remove(os.path.join(self.config["reporting"]["save_path"], file))

if __name__ == "__main__":
    unittest.main()
