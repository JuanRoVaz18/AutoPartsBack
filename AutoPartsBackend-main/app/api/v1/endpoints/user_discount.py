from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import user_discount as crud
from app.api.v1.schemas import user_discount as schema
from app.core.database import get_db
from typing import List

router = APIRouter()   # 👈 SIN PREFIX AQUÍ

@router.post("/", response_model=schema.UserDiscount)
def create_user_discount(user_discount: schema.UserDiscountCreate, db: Session = Depends(get_db)):
    return crud.create_user_discount(db=db, user_discount=user_discount)

@router.get("/", response_model=List[schema.UserDiscount])
def read_user_discounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_user_discounts(db=db, skip=skip, limit=limit)

@router.get("/{user_discount_id}", response_model=schema.UserDiscount)
def read_user_discount(user_discount_id: int, db: Session = Depends(get_db)):
    db_user_discount = crud.get_user_discount(db=db, user_discount_id=user_discount_id)
    if not db_user_discount:
        raise HTTPException(status_code=404, detail="UserDiscount not found")
    return db_user_discount

@router.put("/{user_discount_id}", response_model=schema.UserDiscount)
def update_user_discount(
    user_discount_id: int,
    user_discount: schema.UserDiscountCreate,
    db: Session = Depends(get_db)
):
    db_user_discount = crud.update_user_discount(
        db=db,
        user_discount_id=user_discount_id,
        user_discount=user_discount
    )
    if not db_user_discount:
        raise HTTPException(status_code=404, detail="UserDiscount not found")
    return db_user_discount

@router.delete("/{user_discount_id}", response_model=schema.UserDiscount)
def delete_user_discount(user_discount_id: int, db: Session = Depends(get_db)):
    db_user_discount = crud.delete_user_discount(db=db, user_discount_id=user_discount_id)
    if not db_user_discount:
        raise HTTPException(status_code=404, detail="UserDiscount not found")
    return db_user_discount
