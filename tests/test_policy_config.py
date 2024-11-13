import unittest
from core import policy_config

class TestPolicyConfig(unittest.TestCase):
    def test_load_valid_policy(self):
        # Test loading a valid config.yaml
        config = policy_config.load_policy("config.yaml")
        self.assertIn("rules", config)

    def test_load_missing_policy(self):
        # Test handling of missing config.yaml file
        config = policy_config.load_policy("nonexistent_config.yaml")
        self.assertEqual(config, {})

if __name__ == "__main__":
    unittest.main()
