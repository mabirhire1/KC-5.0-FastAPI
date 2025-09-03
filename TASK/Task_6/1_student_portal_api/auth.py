import json
import os


FILE = "students.json"

def load_students():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}

def save_students(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
