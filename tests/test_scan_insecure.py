import unittest
from core import scan_insecure

class TestScanInsecure(unittest.TestCase):
    def setUp(self):
        self.safe_code = "print('Hello, World!')"
        self.insecure_code = "eval('print(42)')"

    def test_safe_code(self):
        # Check that safe code does not produce security warnings
        with open("safe_code.py", "w") as file:
            file.write(self.safe_code)
        results = scan_insecure.run_bandit_scan("safe_code.py")
        self.assertEqual(len(results), 0)

    def test_insecure_code(self):
        # Check that insecure code produces security warnings
        with open("insecure_code.py", "w") as file:
            file.write(self.insecure_code)
        results = scan_insecure.run_bandit_scan("insecure_code.py")
        self.assertGreater(len(results), 0)

if __name__ == "__main__":
    unittest.main()
