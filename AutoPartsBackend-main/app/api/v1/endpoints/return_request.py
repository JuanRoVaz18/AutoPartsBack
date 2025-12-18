# app/api/v1/endpoints/return_request.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud import return_request as crud
from app.api.v1.schemas import return_request as schema
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schema.ReturnRequest)
def create_return_request(
    rr: schema.ReturnRequestCreate,
    db: Session = Depends(get_db)
):
    return crud.create_return_request(db, rr)

@router.get("/{rr_id}", response_model=schema.ReturnRequest)
def read_return_request(rr_id: int, db: Session = Depends(get_db)):
    rr = crud.get_return_request(db, rr_id)
    if not rr:
        raise HTTPException(status_code=404, detail="ReturnRequest not found")
    return rr

@router.get("/", response_model=List[schema.ReturnRequest])
def read_return_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_return_requests(db, skip, limit)

@router.put("/{rr_id}", response_model=schema.ReturnRequest)
def update_return_request(
    rr_id: int,
    rr: schema.ReturnRequestCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_return_request(db, rr_id, rr)
    if not updated:
        raise HTTPException(status_code=404, detail="ReturnRequest not found")
    return updated

@router.delete("/{rr_id}")
def delete_return_request(rr_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_return_request(db, rr_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ReturnRequest not found")
    return {"ok": True}
