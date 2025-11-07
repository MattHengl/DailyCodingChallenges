import json
import os

def clear_json_file(filename):
    with open(filename, "w") as json_file:
        json_file.write("[]")

def load_json(filename):
    try:
        if not os.path.exists(filename):
            with open(filename, "w", encoding='utf-8') as json_file:
                json_file.write("[]")
            return []
        with open(filename, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
            if data is None:
                return []
            return data
    except Exception as e:
        print(f"Error loading JSON '{filename}': {e}")
        return []

def save_json(filename, save_list):
    print("Saving JSON...")
    try:
        if save_list is None:
            serializable = []
        else:
            serializable = []
            for item in save_list:
                if isinstance(item, dict):
                    serializable.append(item)
                elif hasattr(item, "__dict__"):
                    serializable.append(item.__dict__)
                else:
                    serializable.append(item)
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(serializable, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving JSON '{filename}': {e}")
        return False
    else:
        return True