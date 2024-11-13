# Secure Code Scanner

A Python-based security scanner for analyzing open-source repositories, designed to detect malicious or insecure code. This tool is intended to help users safely download and use open-source tools.

## Features

- **Automated Repository Scanning**: Clone and scan repositories from GitHub.
- **Malicious Code Detection**: Detects risky patterns such as `eval`, `exec`, and unauthorized network connections.
- **Insecure Code Practices**: Scans for hardcoded secrets, insecure cryptographic practices, and dangerous functions.
- **Dependency Scanning**: Checks for vulnerable dependencies using GitHub's Advisory Database.
- **Configurable Security Policies**: Customizable rules and whitelists/blacklists.
- **Output Report**: Generates a detailed JSON report of all flagged issues.
- **CI/CD Integration**: Provides a GitHub Action for automatic scanning.
- **Optional Docker Support**: Dockerized version for secure and isolated scans.

## Getting Started

### Requirements

- Python 3.8 or later
- [Git](https://git-scm.com/) for cloning repositories
- Required Python packages (install via `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/secure-code-scanner.git
    cd secure-code-scanner
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To scan a GitHub repository:

```bash
python scanner.py --repo https://github.com/<username>/<repo>
