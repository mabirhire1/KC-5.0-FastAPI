from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

# User table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password_hash: str

# JobApplication table
class JobApplication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company: str
    position: str
    status: str = "pending"   
    date_applied: date
    user_id: int = Field(foreign_key="user.id")
