# Student Management System (FastAPI)

## Features
- Manage students (CRUD)
- Authentication with JWT
- Request logging middleware
- SQLite database with SQLModel
- CORS for frontend integration

## Folder Structure
student_mgmt/
|─ main.py
├─ database.py
├─ models.py
├─ auth.py
├─ middleware.py
├─ models.py
├─ users.json
├─ README.md
├─ requets.log (created automatically)
├─ students.db (created automatically)
└─ requirements.txt

## App Setup
```bash
git clone <repo-url>
cd student_management_system
pip install -r requirements.txt
```

## Run app
```bash
uvicorn app.main:app --reload
```