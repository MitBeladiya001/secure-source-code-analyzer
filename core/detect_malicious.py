import ast
import re

def detect_malicious_patterns(file_path, config):
    results = []
    with open(file_path, 'r') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id in config['blacklisted_functions']:
                        results.append(f"Suspicious function `{node.func.id}` in {file_path}")
        except SyntaxError:
            print(f"Syntax error in {file_path}")
    return results
