from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from datetime import date
from ..database import get_session
from ..models import JobApplication
from ..auth import get_current_user

router = APIRouter(prefix="/applications", tags=["applications"])

# Add a new job application
@router.post("/")
def add_application(company: str, position: str, status: str = "pending",
                    session: Session = Depends(get_session),
                    user=Depends(get_current_user)):
    app = JobApplication(company=company, position=position,
                         status=status, date_applied=date.today(),
                         user_id=user.id)
    session.add(app)
    session.commit()
    session.refresh(app)
    return app

# List all applications (only for current user)
@router.get("/")
def list_applications(session: Session = Depends(get_session), user=Depends(get_current_user)):
    return session.exec(select(JobApplication).where(JobApplication.user_id == user.id)).all()

# Search applications by status
@router.get("/search")
def search_applications(status: str, session: Session = Depends(get_session), user=Depends(get_current_user)):
    apps = session.exec(
        select(JobApplication).where(JobApplication.user_id == user.id, JobApplication.status == status)
    ).all()
    if not apps:
        raise HTTPException(404, f"No applications found with status '{status}'")
    return apps
