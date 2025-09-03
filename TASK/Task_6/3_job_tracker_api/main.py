from fastapi import FastAPI, Depends, HTTPException
from typing import List
from auth import get_current_user, load_users, save_users, hash_password
from models import JobApplication, User
import json, os

app = FastAPI()

APPLICATIONS_FILE = "applications.json"


def load_applications():
    if os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_applications(data):
    with open(APPLICATIONS_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.post("/register/")
def register(username: str, password: str):
    users = load_users()

    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(username=username, password=hash_password(password))
    users[user.username] = {"password": user.password}
    save_users(users)

    return {"message": f"User {username} registered successfully"}


@app.post("/applications/")
def add_application(application: JobApplication, user=Depends(get_current_user)):
    apps = load_applications()
    username = user["username"]

    if username not in apps:
        apps[username] = []

    apps[username].append(application.dict())
    save_applications(apps)

    return {"message": f"Application for {application.job_title} at {application.company} added"}

@app.get("/applications/", response_model=List[JobApplication])
def get_applications(user=Depends(get_current_user)):
    apps = load_applications()
    return apps.get(user["username"], [])
