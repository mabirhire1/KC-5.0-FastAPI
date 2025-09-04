from fastapi import FastAPI
from .database import init_db
from .middleware import TimingMiddleware
from .routers import users, products, cart

# Create app
app = FastAPI(title="E-Commerce API")

# Init DB
init_db()

# Add timing middleware
app.add_middleware(TimingMiddleware)

# Include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
