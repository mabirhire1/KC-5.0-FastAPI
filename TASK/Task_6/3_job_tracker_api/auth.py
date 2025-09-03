from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
import os
import hashlib


USERS_FILE = "users.json"
security = HTTPBasic()


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    users = load_users()
    username = credentials.username
    password = hash_password(credentials.password)

    if username not in users or users[username]["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"username": username}
