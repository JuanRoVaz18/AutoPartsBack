from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.crud import log as crud
from app.api.v1.schemas import log as schema
from app.core.database import get_db

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.post("/", response_model=schema.Log)
def create_log(log: schema.LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log=log)

@router.get("/{log_id}", response_model=schema.Log)
def read_log(log_id: int, db: Session = Depends(get_db)):
    db_log = crud.get_log(db=db, log_id=log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log

@router.get("/", response_model=List[schema.Log])
def read_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_logs(db=db, skip=skip, limit=limit)

@router.put("/{log_id}", response_model=schema.Log)
def update_log(log_id: int, log: schema.LogCreate, db: Session = Depends(get_db)):
    db_log = crud.update_log(db=db, log_id=log_id, log=log)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log

@router.delete("/{log_id}", response_model=schema.Log)
def delete_log(log_id: int, db: Session = Depends(get_db)):
    db_log = crud.delete_log(db=db, log_id=log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log
