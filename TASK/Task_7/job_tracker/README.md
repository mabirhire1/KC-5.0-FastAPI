# Job Application Tracker API

## Features
* Relational DB with SQLModel (SQLite backend)
* Authentication so users only see their own applications
* CRUD endpoints for job applications
* Search by status
* Error handling for invalid queries
* Middleware that rejects requests if User-Agent header is missing

## Folder Structure
job_tracker/
├─ main.py
├─ database.py
├─ models.py
├─ auth.py
├─ middleware.py
├─ routers/
│  ├─ applications.py
│  └─ users.py
└─ requirements.txt

## Setup
```
git clone <your_repo>
cd job_tracker
pip install -r requirements.txt

```

## Run App
```
uvicorn job_app_tracker.main:app --reload

```