import json
from sqlmodel import Session, select
from models import Note

# Save all notes to a JSON file
def backup_notes(session: Session, filename="notes.json"):
    notes = session.exec(select(Note)).all()
    data = [note.model_dump() for note in notes]  
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, default=str)