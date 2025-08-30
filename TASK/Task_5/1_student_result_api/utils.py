import json, os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}

def save_students(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
