from bandit.core import manager, config as bandit_config

def run_bandit_scan(file_path):
    """Runs Bandit security scans on the specified file."""
    # Initialize Bandit configuration and aggregation type
    conf = bandit_config.BanditConfig()
    bandit_manager = manager.BanditManager(conf, "file")  # Provide config and agg_type

    # Discover files and run tests
    bandit_manager.discover_files([file_path])
    bandit_manager.run_tests()

    # Collect results
    results = [
        f"{issue.fname}:{issue.lineno} - {issue.text}" 
        for issue in bandit_manager.get_issue_list()
    ]
    return results
