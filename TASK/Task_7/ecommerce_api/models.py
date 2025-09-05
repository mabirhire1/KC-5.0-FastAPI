from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

# User Login
class UserLogin(BaseModel):
    username: str
    password: str

# User Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Product table
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    stock: int

# User table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password_hash: str
    is_admin: bool = False

# Order model (not a table, saved to JSON)
class Order(SQLModel):
    product_id: int
    quantity: int
    total_price: float
    username: str
