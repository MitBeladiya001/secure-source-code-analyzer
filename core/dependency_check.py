import requests
import os

def check_dependencies(repo_dir, config):
    results = []
    with open(os.path.join(repo_dir, "requirements.txt"), 'r') as file:
        for line in file:
            package_name, version = line.strip().split("==")
            vulnerabilities = check_vulnerabilities(package_name, version)
            if vulnerabilities:
                results.append(vulnerabilities)
    return results

def check_vulnerabilities(package_name, version):
    url = f"https://api.github.com/advisories/{package_name}/{version}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []
