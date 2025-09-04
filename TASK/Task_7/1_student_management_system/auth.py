import json
from pathlib import Path
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

USERS_FILE = Path(__file__).with_name("users.json")
security = HTTPBasic()
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if not USERS_FILE.exists():
        raise HTTPException(500, "users.json missing")

    users = json.loads(USERS_FILE.read_text())
    for u in users:
        if u["username"] == credentials.username and pwd.verify(credentials.password, u["password"]):
            return {"username": u["username"]}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
