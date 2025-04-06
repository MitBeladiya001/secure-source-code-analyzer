import unittest
import os
from secure_source_code_analyzer.core import scan_insecure

class TestScanInsecure(unittest.TestCase):
    def setUp(self):
        # Create example code files for testing
        self.safe_code_path = "safe_code.py"
        self.insecure_code_path = "insecure_code.py"

        # Write safe code to safe_code.py (no security issues)
        with open(self.safe_code_path, "w") as file:
            file.write("print('Hello, World!')")

        # Write insecure code to insecure_code.py (uses eval, which should be flagged)
        with open(self.insecure_code_path, "w") as file:
            file.write("eval('print(42)')")

    def tearDown(self):
        # Clean up the test files after running tests
        if os.path.exists(self.safe_code_path):
            os.remove(self.safe_code_path)
        if os.path.exists(self.insecure_code_path):
            os.remove(self.insecure_code_path)

    def test_safe_code(self):
        """Test that safe code does not produce any security warnings."""
        results = scan_insecure.run_bandit_scan(self.safe_code_path)
        self.assertEqual(len(results), 0, "Safe code should not produce security warnings.")

    def test_insecure_code(self):
        """Test that insecure code produces security warnings."""
        results = scan_insecure.run_bandit_scan(self.insecure_code_path)
        self.assertGreater(len(results), 0, "Insecure code should produce security warnings.")

if __name__ == "__main__":
    unittest.main()
