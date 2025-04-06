import yaml

def load_policy(file_path='config.yaml'):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {}
    except yaml.YAMLError as e:
        print(f"Error reading configuration file: {e}")
        return {}
