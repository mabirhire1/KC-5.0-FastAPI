from sqlmodel import create_engine, SQLModel, Session
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./contacts.db")

# SQLite config
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

def init_db():
    import models  
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
