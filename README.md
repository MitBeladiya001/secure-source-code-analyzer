# 🚨 Secure Code Scanner 🚨

A production-grade, Python-based security scanner for analyzing open-source repositories, designed to detect malicious or insecure code. Use this tool to confidently integrate third-party code into your projects.

## ✨ Features

- **🔍 Automated Repository Scanning**: Clone and scan GitHub repositories automatically.
- **🚫 Malicious Code Detection**: Detects risky patterns such as `eval`, `exec`, and unauthorized network connections.
- **🔒 Insecure Code Practices**: Scans for hardcoded secrets, insecure cryptographic practices, and unsafe functions.
- **📦 Dependency Scanning**: Checks for outdated or vulnerable dependencies using GitHub's Advisory Database.
- **⚙️ Configurable Security Policies**: Customize rules, whitelists, and blacklists to fit your organizational standards.
- **📊 Comprehensive Reports**: Generates a JSON report with all flagged issues, categorized by severity.
- **CI/CD Integration**: Includes a GitHub Action for automated scanning in CI/CD workflows.
- **🐳 Docker Support**: Runs securely in an isolated environment via Docker, ideal for CI/CD pipelines.

---

## 🚀 Getting Started

### Requirements

- **Python** 3.8 or later
- **Git** for cloning repositories
- Required Python packages (installable via `requirements.txt`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/secure-source-code-analyzer.git
    cd secure-source-code-analyzer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠 Configuration

The tool is configured via a `config.yaml` file, allowing you to customize scanning policies, reporting options, and CI/CD settings. Here’s an example configuration:

```yaml
rules:
  - name: "disallow_eval"
    pattern: "eval"
    severity: "critical"

dependency_policies:
  check_outdated: true
  disallowed_packages:
    - "pycrypto"

reporting:
  output_format: "json"
  verbosity: "high"
  include_timestamp: true
```

---

For more options, refer to the **Documentation** section below.

## 🔧 Usage

To scan a GitHub repository, use the following command:

 ```bash
python scanner.py --repo https://github.com/<username>/<repo>
 ```

Example:

 ```bash
python scanner.py --repo https://github.com/githubtraining/hellogitworld
 ```
This command will:
    -Clone the specified repository.
    -Scan each ```.py``` file for malicious and insecure code practices.
    -Generate a report summarizing any issues found.

## 🧪 Running Tests

To ensure everything is functioning correctly, run the unit tests:

 ```bash
python -m unittest discover -s tests
 ```
This command will automatically discover and execute all tests in the tests/ directory.

---

## 🐳 Docker Usage

Running the tool in Docker provides a secure, isolated environment:

-Build the Docker Image:
 ```bash
docker build -t secure-source-code-analyzer .
 ```
-Run the Scanner in Docker:
```bash
docker run secure-source-code-analyzer --repo https://github.com/<username>/<repo>
```

---

## 🔄 CI/CD Integration with GitHub Actions

Automate security scanning in your CI/CD pipeline with GitHub Actions. The ```.github/workflows/security_scan.yml``` file provided in this repository will automatically run the scanner on each push or pull request.

### Sample GitHub Actions Workflow
```yaml
name: Security Scan and Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python -m unittest discover -s tests
```

## 🤝 Contributing

We welcome contributions to enhance the functionality, performance, and security of this tool! To contribute:

1. Fork the repository.
2. Create a branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature
```
3. Commit your changes with clear messages.
4. Push to your fork and submit a pull request.

--- 

## 📜 Documentation

### Configuration Details
The ```config.yaml``` file offers flexible configuration options, including:

- rules: Define custom scanning rules for risky functions or patterns.
- dependency_policies: Configure dependency checks, including disallowed packages and outdated version policies.
- reporting: Customize output format (e.g., JSON, HTML), verbosity, and save path.
- alerting (optional): Set up notifications via email or Slack for critical issues.
- sandboxing (optional): Enables Docker-based sandboxing for isolated scans.

---

### Output Reports

The tool generates reports in JSON format by default, categorizing issues by severity level and offering insights into each detected vulnerability. Each report includes:

- **Malicious Code**: Lists instances of suspicious patterns detected in code (e.g., usage of `eval`, `exec`, unauthorized network connections).
- **Insecure Code Practices**: Details results from static analysis tools like Bandit, flagging insecure practices such as hardcoded secrets, unsafe cryptographic functions, and insecure file handling.
- **Dependency Vulnerabilities**: Highlights any outdated or vulnerable dependencies based on dependency policies and GitHub's Advisory Database.

An example report entry in JSON format:

```json
{
  "malicious": [
    "example.py:3 - Suspicious use of eval() function",
    "another_file.py:10 - Unauthorized network connection attempt"
  ],
  "insecure": [
    "config.py:5 - Hardcoded secret found: API_KEY",
    "crypto_utils.py:12 - Insecure use of MD5 hashing"
  ],
  "dependencies": [
    {
      "package": "requests",
      "version": "2.18.4",
      "vulnerabilities": [
        {
          "CVE": "CVE-2018-18074",
          "severity": "high",
          "description": "Improper Certificate Validation in Requests"
        }
      ]
    }
  ]
}
```

---

## Additional Configuration Options

### To further customize the scanner’s behavior, you can adjust the following options in config.yaml:

- output_format: Choose between JSON or other formats (e.g., HTML) to suit your reporting requirements.
- verbosity: Set the verbosity level (low, medium, high) to control the amount of detail in the output.
- include_timestamp: Toggle whether to include timestamps in report filenames for better traceability.

---

## ⚖️ License

This project is licensed under the MIT License. See the ```LICENSE``` file for more details.

---

## ☕️ Support Me

If you find this project helpful, please consider supporting my work with a coffee! Your support helps me keep this project maintained and adds motivation to continue improving it. 💙

[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-orange?style=flat-square&logo=buy-me-a-coffee&logoColor=white&link=https://www.buymeacoffee.com/bvvard)](https://www.buymeacoffee.com/bvvard)

---

