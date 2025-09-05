from typing import Optional, List
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

# Database model 
class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: EmailStr
    grades: str = ""

# Input model when creating a new student
class StudentCreate(SQLModel):
    name: str
    age: int
    email: EmailStr
    grades: List[int] = []

# Output model when reading a student
class StudentRead(SQLModel):
    id: int
    name: str
    age: int
    email: EmailStr
    grades: List[int]

# Input model when updating a student
class StudentUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    grades: Optional[List[int]] = None

def list_to_csv(nums: List[int]) -> str:
    return ",".join(str(n) for n in nums)

def csv_to_list(text: str) -> List[int]:
    return [int(x) for x in text.split(",") if x.strip().isdigit()]
