import json
import os

FILE = "applications.json"

def load_data():
    """Load applications from file, return empty dict if not found or error"""
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}

def save_data(data):
    """Save applications to file"""
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
