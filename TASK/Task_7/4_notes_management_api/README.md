# Notes API (Bigger Application + Middleware) 

## Features
* CRUD Endpoints
* Automatic JSON Backup
* CORS Configuration
* Request Counter Middleware

## Folder Structure
notes_api/
├── main.py
├── database.py
├── models.py
├── middleware.py
├── backup.py (auto-created)
├── notes.json
└── requirements.txt

## App Setup
```bash
git clone <repo-url>
cd notes_management_api
pip install -r requirements.txt
```

## Run app
```bash
uvicorn app.main:app --reload
```
