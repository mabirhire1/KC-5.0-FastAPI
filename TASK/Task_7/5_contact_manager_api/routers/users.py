from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import User
from database import get_session
from auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Users"])


@router.post("/register")
def register(user: User, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.username == user.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username taken")
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "User created successfully"}


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}