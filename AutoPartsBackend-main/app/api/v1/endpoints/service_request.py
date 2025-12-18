from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import service_request as crud
from app.api.v1.schemas import service_request as schema
from app.core.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schema.ServiceRequest)
def create_service_request(service_request: schema.ServiceRequestCreate, db: Session = Depends(get_db)):
    return crud.create_service_request(db=db, service_request=service_request)

@router.get("/{service_request_id}", response_model=schema.ServiceRequest)
def read_service_request(service_request_id: int, db: Session = Depends(get_db)):
    db_service_request = crud.get_service_request(db=db, service_request_id=service_request_id)
    if db_service_request is None:
        raise HTTPException(status_code=404, detail="Service Request not found")
    return db_service_request

@router.get("/", response_model=List[schema.ServiceRequest])
def read_service_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_service_requests(db=db, skip=skip, limit=limit)

@router.put("/{service_request_id}", response_model=schema.ServiceRequest)
def update_service_request(service_request_id: int, service_request: schema.ServiceRequestCreate, db: Session = Depends(get_db)):
    db_service_request = crud.update_service_request(db=db, service_request_id=service_request_id, service_request=service_request)
    if db_service_request is None:
        raise HTTPException(status_code=404, detail="Service Request not found")
    return db_service_request

@router.delete("/{service_request_id}", response_model=schema.ServiceRequest)
def delete_service_request(service_request_id: int, db: Session = Depends(get_db)):
    db_service_request = crud.delete_service_request(db=db, service_request_id=service_request_id)
    if db_service_request is None:
        raise HTTPException(status_code=404, detail="Service Request not found")
    return db_service_request
