from fastapi import FastAPI, Depends, HTTPException
from models import Note, LoginRequest
from auth import create_access_token, hash_password, load_users, save_users, get_current_user
import json
import os
from datetime import datetime
from fastapi import Query

app = FastAPI()

NOTES_FILE = "notes.json"

# --- Helpers for notes storage ---
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

# --- User registration ---
@app.post("/register/")
def register(username: str = Query(...), password: str = Query(...)):
    users = load_users()
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username] = hash_password(password)
    save_users(users)
    return {"msg": f"User {username} registered successfully"}

# --- Simplified login ---
@app.post("/login/")
def login(username: str, password: str):
    users = load_users()
    hashed = hash_password(password)
    if username not in users or users[username] != hashed:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

# --- Add a note ---
@app.post("/notes/")
def add_note(note: Note, user=Depends(get_current_user)):
    notes = load_notes()
    notes.setdefault(user["username"], []).append(note.dict())
    save_notes(notes)
    return {"message": "Note added successfully"}

# --- Get own notes ---
@app.get("/notes/")
def get_notes(user=Depends(get_current_user)):
    notes = load_notes()
    return notes.get(user["username"], [])
