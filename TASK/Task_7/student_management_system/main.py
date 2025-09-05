from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import init_db, get_session
from models import Student, StudentCreate, StudentRead, StudentUpdate, list_to_csv, csv_to_list
from auth import get_current_user
from middleware import RequestLoggerMiddleware

# Create app
app = FastAPI(title="Student Management API")

# Add custom middleware
app.add_middleware(RequestLoggerMiddleware)

# Allow frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables on startup
@app.on_event("startup")
def on_startup():
    init_db()

# --- Routes ---

# Create student (protected)
@app.post("/students/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    student = Student(name=payload.name, age=payload.age, email=payload.email, grades=list_to_csv(payload.grades))
    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentRead(id=student.id, name=student.name, age=student.age, email=student.email, grades=csv_to_list(student.grades))

# Read all students (public)
@app.get("/students/", response_model=List[StudentRead])
def list_students(session: Session = Depends(get_session)):
    students = session.exec(select(Student)).all()
    return [StudentRead(id=s.id, name=s.name, age=s.age, email=s.email, grades=csv_to_list(s.grades)) for s in students]

# Update student (protected)
@app.put("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, payload: StudentUpdate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")

    if payload.name is not None: student.name = payload.name
    if payload.age is not None: student.age = payload.age
    if payload.email is not None: student.email = payload.email
    if payload.grades is not None: student.grades = list_to_csv(payload.grades)

    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentRead(id=student.id, name=student.name, age=student.age, email=student.email, grades=csv_to_list(student.grades))

# Delete student (protected)
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    session.delete(student)
    session.commit()
    return
