from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from middleware import LogIPMiddleware
from routers import users, contacts

app = FastAPI(title="Contact Manager API")

# Init DB
init_db()

# CORS
origins = ["http://localhost:3000", "http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IP logging middleware
app.add_middleware(LogIPMiddleware)

# Routers
app.include_router(users.router)
app.include_router(contacts.router)