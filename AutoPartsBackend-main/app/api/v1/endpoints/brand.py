from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import brand as crud
from app.api.v1.schemas import brand as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.Brand)
def create_brand(brand: schema.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db=db, brand=brand)

@router.get("/{brand_id}", response_model=schema.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db=db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.get("/", response_model=List[schema.Brand])
def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_brands(db=db, skip=skip, limit=limit)

@router.put("/{brand_id}", response_model=schema.Brand)
def update_brand(brand_id: int, brand: schema.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.update_brand(db=db, brand_id=brand_id, brand=brand)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.delete("/{brand_id}", response_model=schema.Brand)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.delete_brand(db=db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand
