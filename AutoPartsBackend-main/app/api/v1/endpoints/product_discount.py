from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import product_discount as crud
from app.api.v1.schemas import product_discount as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.ProductDiscount)
def create_product_discount(product_discount: schema.ProductDiscountCreate, db: Session = Depends(get_db)):
    return crud.create_product_discount(db=db, product_discount=product_discount)

@router.get("/{product_discount_id}", response_model=schema.ProductDiscount)
def read_product_discount(product_discount_id: int, db: Session = Depends(get_db)):
    db_product_discount = crud.get_product_discount(db=db, product_discount_id=product_discount_id)
    if db_product_discount is None:
        raise HTTPException(status_code=404, detail="ProductDiscount not found")
    return db_product_discount

@router.get("/", response_model=List[schema.ProductDiscount])
def read_product_discounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_discounts(db=db, skip=skip, limit=limit)

@router.put("/{product_discount_id}", response_model=schema.ProductDiscount)
def update_product_discount(product_discount_id: int, product_discount: schema.ProductDiscountCreate, db: Session = Depends(get_db)):
    db_product_discount = crud.update_product_discount(db=db, product_discount_id=product_discount_id, product_discount=product_discount)
    if db_product_discount is None:
        raise HTTPException(status_code=404, detail="ProductDiscount not found")
    return db_product_discount

@router.delete("/{product_discount_id}", response_model=schema.ProductDiscount)
def delete_product_discount(product_discount_id: int, db: Session = Depends(get_db)):
    db_product_discount = crud.delete_product_discount(db=db, product_discount_id=product_discount_id)
    if db_product_discount is None:
        raise HTTPException(status_code=404, detail="ProductDiscount not found")
    return db_product_discount
