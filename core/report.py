import json
import os
from datetime import datetime

def generate_report(results, config):
    report_path = config['reporting']['save_path']
    os.makedirs(report_path, exist_ok=True)
    # Adjust timestamp format to be compatible with Windows file paths
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = os.path.join(report_path, f"scan_report_{timestamp}.json")
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"Report saved to {filename}")
