import warnings
import logging
import click
import os
import time
import argparse
import sys
from secure_source_code_analyzer.core import clone_repo, detect_malicious, scan_insecure, dependency_check, policy_config, report

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set up logging
logging.basicConfig(
    filename="secure_code_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()

# Helper function for loading bar
def loading_bar(progress, total, length=30):
    percent = int((progress / total) * 100)
    bar = "#" * int((progress / total) * length)
    return f"[{bar:<{length}}] {percent}%"

@click.command()
@click.option("--repo", prompt="GitHub repository URL", help="URL of the GitHub repository")
def main(repo):
    """Secure Code Scanner CLI."""
    print("🔍 Starting Secure Code Scanner...")
    print("🌌 Patience, Padawan. Navigating the Security Force, we are...")  # Displayed immediately
    print("🔄 Performing analysis...")

    try:
        # Load configuration
        config = policy_config.load_policy("config.yaml")
        logger.info("Configuration loaded successfully.")

        # Clone repository
        try:
            repo_dir = clone_repo.clone_repository(repo)
            if not repo_dir:
                click.echo("❌ Failed to clone repository.")
                logger.error("Repository cloning failed.")
                return
            logger.info(f"Repository cloned to {repo_dir}.")
        except Exception as e:
            logger.error(f"Error during repository cloning: {e}")
            click.echo(f"Error during repository cloning: {e}")
            return

        # Initialize result containers
        malicious_results = []
        insecure_results = []
        dependency_results = None  # Explicitly set to None for easy check later

        # Count files for loading bar
        total_files = sum(1 for _, _, files in os.walk(repo_dir) for f in files if f.endswith('.py'))
        scanned_files = 0

        # Scan each .py file in the repository
        try:
            for root, _, files in os.walk(repo_dir):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        logger.info(f"Scanning file: {file_path}")
                        
                        # Detect malicious patterns
                        try:
                            malicious_results += detect_malicious.detect_malicious_patterns(file_path, config)
                        except Exception as e:
                            logger.error(f"Error in malicious code detection for {file_path}: {e}")
                        
                        # Check for insecure code practices
                        try:
                            insecure_results += scan_insecure.run_bandit_scan(file_path)
                        except Exception as e:
                            logger.error(f"Error in insecure code scanning for {file_path}: {e}")
                        
                        # Update progress
                        scanned_files += 1
                        print(loading_bar(scanned_files, total_files), end='\r')
                        time.sleep(5)  # Optional: Simulate delay for loading effect

            # Check for dependency file once after scanning
            try:
                dependency_results = dependency_check.check_dependencies(repo_dir, config)
                if not dependency_results:  # Print only once if dependencies are empty
                    print("⏭️ No requirements.txt found; skipping dependency check.")
                logger.info("Dependency check completed.")
            except Exception as e:
                logger.error(f"Error during dependency checking: {e}")
                click.echo(f"Error during dependency checking: {e}")
                return
            
            print("✅ Scanning complete!")
            
        except Exception as e:
            logger.error(f"Error during file scanning: {e}")
            click.echo(f"Error during file scanning: {e}")
            return

        # Generate report and determine final message
        try:
            results = {
                "malicious": malicious_results,
                "insecure": insecure_results,
                "dependencies": dependency_results or [],
            }
            report_path = report.generate_report(results, config)
            logger.info("Report generated successfully.")

            # Display final summary message in CLI
            if results["malicious"]:
                print("⚠️ WARNING: Malicious code detected! Please check the JSON report for details.")
            elif not results["insecure"] and not results["dependencies"]:
                print("🎉 SUCCESS: No security issues found! Your code is secure and ready for use.")
            
            # Only print the final report path with the emoji
            print(f"📄 Report generated and saved to: {report_path}")
        except Exception as e:
            logger.error(f"Error during report generation: {e}")
            click.echo(f"Error during report generation: {e}")
            return

    finally:
        # Cleanup cloned repository
        if 'repo_dir' in locals() and repo_dir:
            clone_repo.cleanup_repository(repo_dir)
            logger.info("Temporary repository directory cleaned up.")

if __name__ == "__main__":
    main()
