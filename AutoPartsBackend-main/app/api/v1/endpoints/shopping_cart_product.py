from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import shopping_cart_product as crud
from app.api.v1.schemas import shopping_cart_product as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.ShoppingCartProduct)
def create_shopping_cart_product(cart_product: schema.ShoppingCartProductCreate, db: Session = Depends(get_db)):
    return crud.create_shopping_cart_product(db=db, cart_product=cart_product)

@router.get("/{cart_product_id}", response_model=schema.ShoppingCartProduct)
def read_shopping_cart_product(cart_product_id: int, db: Session = Depends(get_db)):
    db_cart_product = crud.get_shopping_cart_product(db=db, cart_product_id=cart_product_id)
    if db_cart_product is None:
        raise HTTPException(status_code=404, detail="ShoppingCartProduct not found")
    return db_cart_product

@router.get("/", response_model=List[schema.ShoppingCartProduct])
def read_shopping_cart_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_shopping_cart_products(db=db, skip=skip, limit=limit)

@router.put("/{cart_product_id}", response_model=schema.ShoppingCartProduct)
def update_shopping_cart_product(cart_product_id: int, cart_product: schema.ShoppingCartProductCreate, db: Session = Depends(get_db)):
    db_cart_product = crud.update_shopping_cart_product(db=db, cart_product_id=cart_product_id, cart_product=cart_product)
    if db_cart_product is None:
        raise HTTPException(status_code=404, detail="ShoppingCartProduct not found")
    return db_cart_product

@router.delete("/{cart_product_id}", response_model=schema.ShoppingCartProduct)
def delete_shopping_cart_product(cart_product_id: int, db: Session = Depends(get_db)):
    db_cart_product = crud.delete_shopping_cart_product(db=db, cart_product_id=cart_product_id)
    if db_cart_product is None:
        raise HTTPException(status_code=404, detail="ShoppingCartProduct not found")
    return db_cart_product
