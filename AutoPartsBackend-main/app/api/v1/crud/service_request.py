from sqlalchemy.orm import Session
from app.api.v1.models import service_request as model
from app.api.v1.schemas import service_request as schema

def create_service_request(db: Session, service_request: schema.ServiceRequestCreate):
    db_service_request = model.ServiceRequest(
        description=service_request.description,
        establishment_id=service_request.establishment_id
    )
    db.add(db_service_request)
    db.commit()
    db.refresh(db_service_request)
    return db_service_request


def get_service_request(db: Session, service_request_id: int):
    return db.query(model.ServiceRequest)\
             .filter(model.ServiceRequest.id == service_request_id)\
             .first()


def get_service_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ServiceRequest)\
             .offset(skip)\
             .limit(limit)\
             .all()


def update_service_request(db: Session, service_request_id: int, service_request: schema.ServiceRequestCreate):
    db_service_request = get_service_request(db, service_request_id)
    if not db_service_request:
        return None

    db_service_request.description = service_request.description
    db_service_request.establishment_id = service_request.establishment_id

    db.commit()
    db.refresh(db_service_request)
    return db_service_request


def delete_service_request(db: Session, service_request_id: int):
    db_service_request = get_service_request(db, service_request_id)
    if not db_service_request:
        return None

    db.delete(db_service_request)
    db.commit()
    return db_service_request
