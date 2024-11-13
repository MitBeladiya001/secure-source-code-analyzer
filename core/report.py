import json
import os
from datetime import datetime

def generate_report(results, config):
    report_path = config['reporting']['save_path']
    os.makedirs(report_path, exist_ok=True)
    filename = os.path.join(report_path, f"scan_report_{datetime.now().isoformat()}.json")
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"Report saved to {filename}")
