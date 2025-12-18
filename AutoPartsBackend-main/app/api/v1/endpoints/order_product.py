from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud import order_product as crud
from app.api.v1.schemas import order_product as schema
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schema.OrderProduct)
def create_order_product(
    order_product: schema.OrderProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order_product(db, order_product)


@router.get("/", response_model=List[schema.OrderProduct])
def read_order_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_order_products(db, skip, limit)


@router.get("/{order_id}/{product_id}", response_model=schema.OrderProduct)
def read_order_product(
    order_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):
    result = crud.get_order_product(db, order_id, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderProduct not found")
    return result


@router.put("/{order_id}/{product_id}", response_model=schema.OrderProduct)
def update_order_product(
    order_id: int,
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):
    result = crud.update_order_product(db, order_id, product_id, quantity)
    if not result:
        raise HTTPException(status_code=404, detail="OrderProduct not found")
    return result


@router.delete("/{order_id}/{product_id}")
def delete_order_product(
    order_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_order_product(db, order_id, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="OrderProduct not found")
    return {"detail": "Deleted successfully"}
