import unittest
import os
from core import clone_repo

class TestCloneRepo(unittest.TestCase):
    def setUp(self):
        # Example repository URL for testing
        self.repo_url = "https://github.com/githubtraining/hellogitworld"  # Public, simple repo for test purposes

    def test_clone_repository(self):
        # Test successful cloning
        repo_dir = clone_repo.clone_repository(self.repo_url)
        self.assertIsNotNone(repo_dir)
        self.assertTrue(os.path.isdir(repo_dir))
        clone_repo.cleanup_repository(repo_dir)

    def test_cleanup_repository(self):
        # Test cleanup functionality
        repo_dir = clone_repo.clone_repository(self.repo_url)
        clone_repo.cleanup_repository(repo_dir)
        self.assertFalse(os.path.exists(repo_dir))

if __name__ == "__main__":
    unittest.main()
