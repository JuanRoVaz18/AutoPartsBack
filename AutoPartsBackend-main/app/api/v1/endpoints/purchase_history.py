from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud import purchase_history as crud
from app.api.v1.schemas import purchase_history as schema
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schema.PurchaseHistory)
def create_purchase_history(
    data: schema.PurchaseHistoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_purchase_history(db, data)

@router.get("/{history_id}", response_model=schema.PurchaseHistory)
def read_purchase_history(history_id: int, db: Session = Depends(get_db)):
    obj = crud.get_purchase_history(db, history_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Purchase history not found")
    return obj

@router.get("/", response_model=List[schema.PurchaseHistory])
def read_purchase_histories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_purchase_histories(db, skip, limit)

@router.delete("/{history_id}", response_model=schema.PurchaseHistory)
def delete_purchase_history(history_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_purchase_history(db, history_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Purchase history not found")
    return obj
