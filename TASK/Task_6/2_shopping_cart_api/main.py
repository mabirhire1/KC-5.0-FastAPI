from fastapi import FastAPI, Depends, HTTPException
from auth import get_current_user, require_admin, load_users, save_users, hash_password
import json
import os

app = FastAPI()

PRODUCTS_FILE = "products.json"
CART_FILE = "cart.json"

# --- Helpers for JSON storage --- #
def load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}

def save(file_name: str, data: dict):    
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# ---------- User Management ----------
@app.post("/register/")
def register(username: str, password: str, role: str = "customer"):
    users = load_users()

    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    if role not in ["admin", "customer"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    users[username] = {"password": hash_password(password), "role": role}
    save_users(users)

    return {"message": f"User {username} registered successfully as {role}"}

# ---------- Admin Endpoints ----------
@app.post("/admin/add_product/")
def add_product(product_id: str, name: str, price: float, user=Depends(require_admin)):   
    products = load(PRODUCTS_FILE)

    if product_id in products:
        raise HTTPException(status_code=400, detail="Product already exists")

    products[product_id] = {"name": name, "price": price}
    save(PRODUCTS_FILE, products)

    return {"message": f"Product '{name}' added successfully"}

# ---------- Public Endpoints ----------
@app.get("/products/")
def list_products():   
    return load(PRODUCTS_FILE)

# ---------- Customer Endpoints ----------
@app.post("/cart/add/")
def add_to_cart(product_id: str, quantity: int, user=Depends(get_current_user)):  
    products = load(PRODUCTS_FILE)
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = load(CART_FILE)
    username = user["username"]

    if username not in cart:
        cart[username] = []

    cart[username].append({"product_id": product_id, "quantity": quantity})
    save(CART_FILE, cart)

    return {
        "message": f"Added {quantity} x {products[product_id]['name']} to {username}'s cart"
    }

@app.get("/cart/")
def view_cart(user=Depends(get_current_user)):    
    cart = load(CART_FILE)
    return {user["username"]: cart.get(user["username"], [])}
