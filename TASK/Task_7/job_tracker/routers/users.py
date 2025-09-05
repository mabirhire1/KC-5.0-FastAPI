from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import User
from ..auth import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/users", tags=["users"])

# Register a user
@router.post("/register")
def register(username: str, password: str, session: Session = Depends(get_session)):
    if session.exec(select(User).where(User.username == username)).first():
        raise HTTPException(400, "Username already taken")
    user = User(username=username, password_hash=hash_password(password))
    session.add(user)
    session.commit()
    return {"msg": "User registered successfully"}

# Login
@router.post("/login")
def login(username: str, password: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
