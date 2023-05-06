import json
import os


def get_api_key(name):
    if os.path.exists("api_key.json"):
        with open("api_key.json") as f:
            data = json.load(f)
            return data[name]
    return ""


def set_api_key(name, value):
    mode = "r+"
    if not os.path.exists("api_key.json"):
        mode = "w"
    with open("api_key.json", mode) as f:
        if mode == "r+":
            data = json.load(f)
        else:
            data = {}
        data[name] = value
        json.dump(data, f, indent=4)
