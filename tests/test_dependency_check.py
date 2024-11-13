import requests

def check_dependencies(requirements_file, config):
    results = []
    with open(requirements_file, 'r') as file:
        for line in file:
            package_name, version = line.strip().split("==")
            vulnerabilities = check_vulnerabilities(package_name, version)
            if vulnerabilities:
                results.append(vulnerabilities)
    return results

def check_vulnerabilities(package_name, version):
    # Mocked URL; in real-world use, this would connect to a vulnerability API
    url = f"https://api.github.com/advisories/{package_name}/{version}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []
