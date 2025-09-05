from fastapi import FastAPI
from .database import init_db
from .routers import users, applications
from .middleware import UserAgentMiddleware

app = FastAPI(title="Job Application Tracker")

# Init database
init_db()

# Add middleware
app.add_middleware(UserAgentMiddleware)

# Include routers
app.include_router(users.router)
app.include_router(applications.router)
