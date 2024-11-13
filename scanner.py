import click
from core import clone_repo, detect_malicious, scan_insecure, dependency_check, policy_config, report

@click.command()
@click.option("--repo", prompt="GitHub repository URL", help="URL of the GitHub repository")
def main(repo):
    """Secure Source Code Scanner CLI."""
    config = policy_config.load_policy("config.yaml")

    # Clone repository
    repo_dir = clone_repo.clone_repository(repo)
    if not repo_dir:
        click.echo("Failed to clone repository.")
        return

    # Scan repository for malicious code
    malicious_results = []
    insecure_results = []
    
    # Perform scans on each .py file
    for root, _, files in os.walk(repo_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                malicious_results += detect_malicious.detect_malicious_patterns(file_path, config)
                insecure_results += scan_insecure.run_bandit_scan(file_path)

    # Check dependencies
    dependency_results = dependency_check.check_dependencies(repo_dir, config)

    # Generate report
    results = {
        "malicious": malicious_results,
        "insecure": insecure_results,
        "dependencies": dependency_results
    }
    report.generate_report(results, config)

    # Cleanup cloned repository
    clone_repo.cleanup_repository(repo_dir)

if __name__ == "__main__":
    main()
