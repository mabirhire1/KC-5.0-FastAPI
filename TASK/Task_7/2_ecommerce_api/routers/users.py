from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from ..database import get_session
from ..models import User
from ..auth import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/users", tags=["users"])

# Register a new user
@router.post("/register")
def register(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    # Check if username already exists
    if session.exec(select(User).where(User.username == data.username)).first():
        raise HTTPException(400, "Username already taken")

    user = User(username=data.username, password_hash=hash_password(data.password))
    session.add(user)
    session.commit()
    return {"msg": "User registered successfully"}

# Login and return a JWT token
@router.post("/token")
def login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == data.username)).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Invalid username or password")

    # Include username + is_admin in token
    token = create_access_token({"sub": user.username, "is_admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer"}
