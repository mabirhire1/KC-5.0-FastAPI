import json, os, math

FILE = "cart.json"

def load_cart():
    """Load cart from file or return empty dict"""
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_cart(cart):
    """Save cart to file"""
    with open(FILE, "w") as f:
        json.dump(cart, f, indent=4)

def load_products():
    """Return available products"""
    return {
        "1": {"id": 1, "name": "Turkey", "price": 1200.50},
        "2": {"id": 2, "name": "Butter", "price": 500.99},
        "3": {"id": 3, "name": "Spices", "price": 79.99},
    }

def add_to_cart(product_id, qty, products):
    """Add a product to cart"""
    cart = load_cart()
    pid = str(product_id)

    if pid not in products:
        return {"error": "Product not found"}

    if pid in cart:
        cart[pid]["qty"] += qty
    else:
        cart[pid] = {
            "name": products[pid]["name"],
            "price": products[pid]["price"],
            "qty": qty
        }

    save_cart(cart)
    return cart

def checkout():
    """Return total price and cart contents"""
    cart = load_cart()
    total = sum(item["price"] * item["qty"] for item in cart.values())
    return {"total": math.ceil(total), "cart": cart}
