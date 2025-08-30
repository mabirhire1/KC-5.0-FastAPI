from fastapi import FastAPI, HTTPException
from models import Student
from utils import load_students, save_students

app = FastAPI()
students = load_students()

def calculate_grade(scores):
    avg = sum(scores.values()) / len(scores)
    if avg >= 80: grade = "A"
    elif avg >= 70: grade = "B"
    elif avg >= 60: grade = "C"
    elif avg >= 50: grade = "D"
    elif avg >= 40: grade = "E"
    else: grade = "F"
    return avg, grade

@app.post("/students/")
def add_student(student: Student):
    try:
        avg, grade = calculate_grade(student.subject_scores)
        student.average, student.grade = avg, grade
        students[student.name] = student.dict()
        save_students(students)
        return {"message": "Student added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students/{name}")
def get_student(name: str):
    if name not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[name]

@app.get("/students/")
def list_students():
    return students