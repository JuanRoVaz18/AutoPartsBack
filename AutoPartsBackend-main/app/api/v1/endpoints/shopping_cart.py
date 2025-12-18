from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import shopping_cart as crud
from app.api.v1.schemas import shopping_cart as schema
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/shopping-cart", tags=["Shopping Cart"])

@router.post("/", response_model=schema.ShoppingCart)
def create_shopping_cart(cart: schema.ShoppingCartCreate, db: Session = Depends(get_db)):
    return crud.create_shopping_cart(db=db, cart=cart)

@router.get("/{cart_id}", response_model=schema.ShoppingCart)
def read_shopping_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.get_shopping_cart(db=db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Shopping cart not found")
    return db_cart

@router.get("/", response_model=List[schema.ShoppingCart])
def read_shopping_carts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_shopping_carts(db=db, skip=skip, limit=limit)

@router.delete("/{cart_id}", response_model=schema.ShoppingCart)
def delete_shopping_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.delete_shopping_cart(db=db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Shopping cart not found")
    return db_cart
