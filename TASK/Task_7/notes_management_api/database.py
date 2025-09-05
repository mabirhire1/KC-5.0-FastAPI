from sqlmodel import create_engine, SQLModel, Session

# Use SQLite database file
DATABASE_URL = "sqlite:///./notes.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create tables if not exist
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Provide DB session for routes
def get_session():
    with Session(engine) as session:
        yield session
