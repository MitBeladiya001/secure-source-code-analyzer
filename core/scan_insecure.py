from bandit.core import manager

def run_bandit_scan(file_path):
    bandit_manager = manager.BanditManager()
    bandit_manager.discover_files([file_path])
    bandit_manager.run_tests()
    results = [f"{issue.fname}:{issue.lineno} - {issue.text}" for issue in bandit_manager.get_issue_list()]
    return results
