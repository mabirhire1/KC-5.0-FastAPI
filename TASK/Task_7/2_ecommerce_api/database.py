from sqlmodel import SQLModel, create_engine, Session

# SQLite database file
engine = create_engine("sqlite:///shop.db", echo=False)

# Create all tables
def init_db():
    SQLModel.metadata.create_all(engine)

# Session generator (used in routes)
def get_session():
    with Session(engine) as session:
        yield session
