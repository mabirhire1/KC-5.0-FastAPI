from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    username: str
    password: str  
    grades: List[int] = []
