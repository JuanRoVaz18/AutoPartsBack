from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import address as crud
from app.api.v1.schemas import address as schema
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/addresses", tags=["Addresses"])

@router.post("/", response_model=schema.Address)
def create_address(address: schema.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)

@router.get("/{address_id}", response_model=schema.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db=db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.get("/", response_model=List[schema.Address])
def read_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_addresses(db=db, skip=skip, limit=limit)

@router.put("/{address_id}", response_model=schema.Address)
def update_address(address_id: int, address: schema.AddressCreate, db: Session = Depends(get_db)):
    db_address = crud.update_address(db=db, address_id=address_id, address=address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.delete("/{address_id}", response_model=schema.Address)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.delete_address(db=db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
