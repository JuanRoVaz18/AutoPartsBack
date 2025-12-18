from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud import order_coupon as crud
from app.api.v1.schemas import order_coupon as schema
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schema.OrderCoupon)
def create_order_coupon(
    order_coupon: schema.OrderCouponCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order_coupon(db, order_coupon)


@router.get("/", response_model=List[schema.OrderCoupon])
def read_order_coupons(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_order_coupons(db, skip, limit)


@router.get("/{order_id}/{coupon_id}", response_model=schema.OrderCoupon)
def read_order_coupon(
    order_id: int,
    coupon_id: int,
    db: Session = Depends(get_db)
):
    result = crud.get_order_coupon(db, order_id, coupon_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderCoupon not found")
    return result


@router.delete("/{order_id}/{coupon_id}")
def delete_order_coupon(
    order_id: int,
    coupon_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_order_coupon(db, order_id, coupon_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderCoupon not found")
    return {"detail": "Deleted successfully"}
