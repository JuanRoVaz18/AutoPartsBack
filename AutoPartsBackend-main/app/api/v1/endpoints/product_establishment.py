from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import product_establishment as crud
from app.api.v1.schemas import product_establishment as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.ProductEstablishment)
def create_product_establishment(establishment: schema.ProductEstablishmentCreate, db: Session = Depends(get_db)):
    return crud.create_product_establishment(db=db, establishment=establishment)

@router.get("/{establishment_id}", response_model=schema.ProductEstablishment)
def read_product_establishment(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = crud.get_product_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="ProductEstablishment not found")
    return db_establishment

@router.get("/", response_model=List[schema.ProductEstablishment])
def read_product_establishments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_establishments(db=db, skip=skip, limit=limit)

@router.put("/{establishment_id}", response_model=schema.ProductEstablishment)
def update_product_establishment(establishment_id: int, establishment: schema.ProductEstablishmentCreate, db: Session = Depends(get_db)):
    db_establishment = crud.update_product_establishment(db=db, establishment_id=establishment_id, establishment=establishment)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="ProductEstablishment not found")
    return db_establishment

@router.delete("/{establishment_id}", response_model=schema.ProductEstablishment)
def delete_product_establishment(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = crud.delete_product_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="ProductEstablishment not found")
    return db_establishment
