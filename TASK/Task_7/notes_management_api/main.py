from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import Note, NoteCreate
from database import create_db_and_tables, get_session
from backup import backup_notes
from middleware import RequestCounterMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Notes API")

# Allow requests from frontend apps
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add middleware for counting requests
app.add_middleware(RequestCounterMiddleware)

# Create DB tables when app starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- Routes ---

@app.post("/notes/", response_model=Note)
def create_note(note_data: NoteCreate, session: Session = Depends(get_session)):
    note = Note(**note_data.model_dump())  # Create Note instance with validated data; created_at defaults automatically
    session.add(note)
    session.commit()
    session.refresh(note)
    backup_notes(session)
    return note

@app.get("/notes/", response_model=list[Note])
def get_notes(session: Session = Depends(get_session)):
    return session.exec(select(Note)).all()

@app.get("/notes/{note_id}", response_model=NoteCreate)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    backup_notes(session)
    return {"message": "Note deleted successfully"}
