from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.crud import status as crud
from app.api.v1.schemas.status import Status, StatusCreate
from app.core.database import get_db

router = APIRouter(prefix="/status", tags=["Status"])


@router.post("/", response_model=Status)
def create_status(status: StatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db, status)


@router.get("/", response_model=List[Status])
def read_statuses(db: Session = Depends(get_db)):
    return crud.get_statuses(db)


@router.get("/{status_id}", response_model=Status)
def read_status(status_id: int, db: Session = Depends(get_db)):
    db_status = crud.get_status(db, status_id)
    if not db_status:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status


@router.put("/{status_id}", response_model=Status)
def update_status(status_id: int, status: StatusCreate, db: Session = Depends(get_db)):
    db_status = crud.update_status(db, status_id, status)
    if not db_status:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status


@router.delete("/{status_id}", response_model=Status)
def delete_status(status_id: int, db: Session = Depends(get_db)):
    db_status = crud.delete_status(db, status_id)
    if not db_status:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status
