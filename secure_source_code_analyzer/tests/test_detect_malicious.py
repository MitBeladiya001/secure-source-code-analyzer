import unittest
from secure_source_code_analyzer.core import detect_malicious

class TestDetectMalicious(unittest.TestCase):
    def setUp(self):
        # Sample configurations and code files
        self.config = {
            "blacklisted_functions": ["eval", "exec"]
        }
        self.safe_code = "print('Hello, World!')"
        self.malicious_code = "eval('print(42)')"

    def test_safe_code(self):
        # Check that safe code does not produce warnings
        with open("safe_code.py", "w") as file:
            file.write(self.safe_code)
        results = detect_malicious.detect_malicious_patterns("safe_code.py", self.config)
        self.assertEqual(len(results), 0)

    def test_malicious_code(self):
        # Check that malicious code is detected
        with open("malicious_code.py", "w") as file:
            file.write(self.malicious_code)
        results = detect_malicious.detect_malicious_patterns("malicious_code.py", self.config)
        self.assertGreater(len(results), 0)

if __name__ == "__main__":
    unittest.main()
