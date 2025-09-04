import json, os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import Product, Order
from ..auth import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

ORDERS_FILE = "ecommerce_api/orders.json"

# Add product to cart (actually creates an order)
@router.post("/add")
def add_to_cart(product_id: int, quantity: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        raise HTTPException(404, "Product not found")
    if product.stock < quantity:
        raise HTTPException(400, "Not enough stock")

    # Deduct stock
    product.stock -= quantity
    session.add(product)
    session.commit()

    # Create order
    order = Order(
        product_id=product.id,
        quantity=quantity,
        total_price=product.price * quantity,
        username=user["username"]
    )

    # Save order to JSON
    orders = []
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
    orders.append(order.dict())
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)

    return {"msg": "Order placed", "order": order}
