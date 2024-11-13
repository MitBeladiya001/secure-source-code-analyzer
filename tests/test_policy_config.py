import unittest
from core import policy_config

class TestPolicyConfig(unittest.TestCase):
    def test_load_policy(self):
        config = policy_config.load_policy("config.yaml")
        self.assertIn("rules", config)
        self.assertIn("reporting", config)
        self.assertIn("dependency_policies", config)

if __name__ == "__main__":
    unittest.main()
