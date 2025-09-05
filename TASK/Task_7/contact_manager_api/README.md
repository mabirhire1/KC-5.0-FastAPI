# Contact Manager API
## Folder Structure
contact_manager/
├── main.py
├── database.py
├── models.py
├── middleware.py
├── auth.py
├─ routers/
│  └─ contacts.py
│  └─ users.py
├── contact.db (automatically created)
├── requirements.txt
└── README.md

## Run App Locally
pip install -r requirements.txt
uvicorn app.main:app --reload