from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import establishment as crud
from app.api.v1.schemas import establishment as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.Establishment)
def create_establishment(establishment: schema.EstablishmentCreate, db: Session = Depends(get_db)):
    return crud.create_establishment(db=db, establishment=establishment)

@router.get("/{establishment_id}", response_model=schema.Establishment)
def read_establishment(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = crud.get_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    return db_establishment

@router.get("/", response_model=List[schema.Establishment])
def read_establishments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_establishments(db=db, skip=skip, limit=limit)

@router.put("/{establishment_id}", response_model=schema.Establishment)
def update_establishment(establishment_id: int, establishment: schema.EstablishmentCreate, db: Session = Depends(get_db)):
    db_establishment = crud.update_establishment(db=db, establishment_id=establishment_id, establishment=establishment)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    return db_establishment

@router.delete("/{establishment_id}", response_model=schema.Establishment)
def delete_establishment(establishment_id: int, db: Session = Depends(get_db)):
    db_establishment = crud.delete_establishment(db=db, establishment_id=establishment_id)
    if db_establishment is None:
        raise HTTPException(status_code=404, detail="Establishment not found")
    return db_establishment
