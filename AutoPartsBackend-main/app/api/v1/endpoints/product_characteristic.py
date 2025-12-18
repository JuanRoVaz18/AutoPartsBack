from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import product_characteristic as crud
from app.api.v1.schemas import product_characteristic as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.ProductCharacteristic)
def create_product_characteristic(characteristic: schema.ProductCharacteristicCreate, db: Session = Depends(get_db)):
    return crud.create_product_characteristic(db=db, characteristic=characteristic)

@router.get("/{characteristic_id}", response_model=schema.ProductCharacteristic)
def read_product_characteristic(characteristic_id: int, db: Session = Depends(get_db)):
    db_characteristic = crud.get_product_characteristic(db=db, characteristic_id=characteristic_id)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic

@router.get("/", response_model=List[schema.ProductCharacteristic])
def read_product_characteristics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_characteristics(db=db, skip=skip, limit=limit)

@router.put("/{characteristic_id}", response_model=schema.ProductCharacteristic)
def update_product_characteristic(characteristic_id: int, characteristic: schema.ProductCharacteristicCreate, db: Session = Depends(get_db)):
    db_characteristic = crud.update_product_characteristic(db=db, characteristic_id=characteristic_id, characteristic=characteristic)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic

@router.delete("/{characteristic_id}", response_model=schema.ProductCharacteristic)
def delete_product_characteristic(characteristic_id: int, db: Session = Depends(get_db)):
    db_characteristic = crud.delete_product_characteristic(db=db, characteristic_id=characteristic_id)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic
