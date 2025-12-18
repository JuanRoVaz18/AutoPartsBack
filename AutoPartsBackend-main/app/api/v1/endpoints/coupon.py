from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import coupon as crud
from app.api.v1.schemas import coupon as schema
from app.core.database import get_db
from typing import List
router = APIRouter()

@router.post("/", response_model=schema.Coupon)
def create_coupon(coupon: schema.CouponCreate, db: Session = Depends(get_db)):
    return crud.create_coupon(db=db, coupon=coupon)

@router.get("/{coupon_id}", response_model=schema.Coupon)
def read_coupon(coupon_id: int, db: Session = Depends(get_db)):
    db_coupon = crud.get_coupon(db=db, coupon_id=coupon_id)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon

@router.get("/", response_model=List[schema.Coupon])
def read_coupons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_coupons(db=db, skip=skip, limit=limit)

@router.put("/{coupon_id}", response_model=schema.Coupon)
def update_coupon(coupon_id: int, coupon: schema.CouponCreate, db: Session = Depends(get_db)):
    db_coupon = crud.update_coupon(db=db, coupon_id=coupon_id, coupon=coupon)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon

@router.delete("/{coupon_id}", response_model=schema.Coupon)
def delete_coupon(coupon_id: int, db: Session = Depends(get_db)):
    db_coupon = crud.delete_coupon(db=db, coupon_id=coupon_id)
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon
