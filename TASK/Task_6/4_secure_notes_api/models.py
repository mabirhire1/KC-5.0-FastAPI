from pydantic import BaseModel

class Note(BaseModel):
    title: str
    content: str
    date: str

class LoginRequest(BaseModel):
    username: str
    password: str
