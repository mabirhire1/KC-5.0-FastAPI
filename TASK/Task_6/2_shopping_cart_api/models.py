from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str  

class Product(BaseModel):
    name: str
    price: float

class CartItem(BaseModel):
    product: str
    quantity: int
