import json
import os
from datetime import datetime

def generate_report(results, config):
    """Generates a report in JSON format and saves it to the specified file."""

    # Check if malicious content is detected
    if results["malicious"]:
        results["message"] = (
            "⚠️ WARNING: Malicious code detected! Please review the findings and address potential security issues in your code to ensure safety."
        )
    
    # Check if no issues were found to add a success message
    elif not results["insecure"] and not results["dependencies"]:
        results["message"] = (
            "🎉 SUCCESS! No security issues found! Your code is secure, clean, and ready for use."
        )

    # Retrieve report directory from config or default to "reports"
    report_dir = config.get("reporting", {}).get("report_directory", "reports")
    os.makedirs(report_dir, exist_ok=True)

    # Generate a filename with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = os.path.join(report_dir, f"scan_report_{timestamp}.json")

    # Write the JSON report to the file
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

    # Return the path to the generated report for logging and CLI output
    return filename
