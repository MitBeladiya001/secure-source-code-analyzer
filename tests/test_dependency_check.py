import unittest
from core import dependency_check

class TestDependencyCheck(unittest.TestCase):
    def setUp(self):
        # Create mock requirements.txt files
        self.safe_requirements = "requests==2.25.1\n"
        self.vulnerable_requirements = "pycrypto==2.6.1\n"
        with open("safe_requirements.txt", "w") as file:
            file.write(self.safe_requirements)
        with open("vulnerable_requirements.txt", "w") as file:
            file.write(self.vulnerable_requirements)
        self.config = {
            "dependency_policies": {
                "disallowed_packages": ["pycrypto"]
            }
        }

    def test_safe_requirements(self):
        results = dependency_check.check_dependencies("safe_requirements.txt", self.config)
        self.assertEqual(len(results), 0)

    def test_vulnerable_requirements(self):
        results = dependency_check.check_dependencies("vulnerable_requirements.txt", self.config)
        self.assertGreater(len(results), 0)

if __name__ == "__main__":
    unittest.main()
