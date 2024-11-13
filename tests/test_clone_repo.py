import unittest
from unittest.mock import patch
from core import clone_repo

class TestCloneRepo(unittest.TestCase):
    @patch('core.clone_repo.git.Repo.clone_from')
    def test_clone_repository_failure(self, mock_clone_from):
        # Mock a failure in git.Repo.clone_from to raise an exception
        mock_clone_from.side_effect = Exception("Cloning failed")
        
        repo_url = "https://github.com/nonexistent/repo"
        result = clone_repo.clone_repository(repo_url)
        
        self.assertIsNone(result)
    
    def test_cleanup_repository(self):
        # Ensure cleanup works without errors even on a non-existent path
        clone_repo.cleanup_repository("nonexistent_path")

if __name__ == "__main__":
    unittest.main()
