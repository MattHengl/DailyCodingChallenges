import json
import os

def load_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def save_json(filename, content):
    try:
        if os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(content)
        else:
            with open(filename, "w") as f:
                f.write(content)
    except:
        return False
    else:
        return True