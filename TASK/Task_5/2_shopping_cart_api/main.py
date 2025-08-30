from fastapi import FastAPI, HTTPException
from cart import add_to_cart, checkout, load_products

app = FastAPI()

@app.get("/products/")
def list_products():
    return load_products()

@app.post("/cart/add")
def add_item(product_id: int, qty: int):
    products = load_products()
    result = add_to_cart(product_id, qty, products)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.get("/cart/checkout")
def checkout_cart():
    return checkout()
