from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from models import Student
from auth import load_students, save_students

app = FastAPI()

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    students = load_students()
    user = students.get(credentials.username)
    if not user or not pwd_context.verify(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username


@app.post("/register/")
def register(student: Student):
    students = load_students()
    if student.username in students:
        raise HTTPException(status_code=400, detail="User already exists")
    

    student.password = pwd_context.hash(student.password)
    students[student.username] = student.dict()
    save_students(students)
    
    return {"message": "Student registered successfully"}


@app.post("/login/")
def login(username: str = Depends(authenticate)):
    return {"message": f"Welcome {username}"}


@app.get("/grades/")
def get_grades(username: str = Depends(authenticate)):
    students = load_students()
    return {"grades": students[username]["grades"]}
