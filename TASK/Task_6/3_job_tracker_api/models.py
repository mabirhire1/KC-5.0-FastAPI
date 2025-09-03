from pydantic import BaseModel
from typing import List

class JobApplication(BaseModel):
    title: str
    company: str
    date_applied: str
    status: str

class User(BaseModel):
    username: str
    password: str     
