# app/api/v1/crud/return_request.py
from sqlalchemy.orm import Session
from app.api.v1.models import return_request as model
from app.api.v1.schemas import return_request as schema

def create_return_request(db: Session, rr: schema.ReturnRequestCreate):
    db_rr = model.ReturnRequest(
        reason=rr.reason,
        return_status=rr.return_status,
        order_id=rr.order_id
    )
    db.add(db_rr)
    db.commit()
    db.refresh(db_rr)
    return db_rr

def get_return_request(db: Session, rr_id: int):
    return db.query(model.ReturnRequest).filter(model.ReturnRequest.id == rr_id).first()

def get_return_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ReturnRequest).offset(skip).limit(limit).all()

def update_return_request(db: Session, rr_id: int, rr: schema.ReturnRequestCreate):
    db_rr = get_return_request(db, rr_id)
    if not db_rr:
        return None

    db_rr.reason = rr.reason
    db_rr.return_status = rr.return_status
    db.commit()
    db.refresh(db_rr)
    return db_rr

def delete_return_request(db: Session, rr_id: int):
    db_rr = get_return_request(db, rr_id)
    if not db_rr:
        return None

    db.delete(db_rr)
    db.commit()
    return db_rr
