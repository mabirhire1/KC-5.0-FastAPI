# from sqlmodel import SQLModel, Field
# from datetime import datetime

# # Note table model
# class NoteCreate(SQLModel, table=True):
#     #id: int | None = Field(default=None, primary_key=True)
#     title: str
#     content: str
#     #created_at: datetime = Field(default_factory=datetime.utcnow)
from sqlmodel import SQLModel, Field
from datetime import datetime

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class NoteCreate(SQLModel):  # Removed table=True
    title: str
    content: str