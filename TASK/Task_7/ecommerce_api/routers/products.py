from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import Product
from ..auth import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

# List all products
@router.get("/")
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()

# Add product (only admin)
@router.post("/")
def add_product(product: Product, session: Session = Depends(get_session), user=Depends(get_current_user)):
    if not user["is_admin"]:
        raise HTTPException(403, "Only admin can add products")
    session.add(product)
    session.commit()
    return {"msg": "Product added"}
