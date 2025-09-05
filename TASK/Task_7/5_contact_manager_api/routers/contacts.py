from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Contact, User
from database import get_session
from auth import get_current_user

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.post("/")
def create_contact(
    contact: Contact,
    username: str = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    contact.user_id = user.id
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return contact


@router.get("/")
def list_contacts(
    username: str = Depends(get_current_user), session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.username == username)).first()
    return session.exec(select(Contact).where(Contact.user_id == user.id)).all()


@router.put("/{contact_id}")
def update_contact(
    contact_id: int,
    new_data: Contact,
    username: str = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    contact = session.get(Contact, contact_id)
    if not contact or contact.owner.username != username:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact.name = new_data.name
    contact.email = new_data.email
    contact.phone = new_data.phone
    session.add(contact)
    session.commit()
    return contact


@router.delete("/{contact_id}")
def delete_contact(
    contact_id: int,
    username: str = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    contact = session.get(Contact, contact_id)
    if not contact or contact.owner.username != username:
        raise HTTPException(status_code=404, detail="Contact not found")
    session.delete(contact)
    session.commit()
    return {"message": "Contact deleted"}
