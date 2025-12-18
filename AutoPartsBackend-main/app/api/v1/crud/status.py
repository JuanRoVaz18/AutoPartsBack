from sqlalchemy.orm import Session
from app.api.v1.models.status import Status
from app.api.v1.schemas.status import StatusCreate


def create_status(db: Session, status: StatusCreate):
    db_status = Status(name=status.name)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def get_status(db: Session, status_id: int):
    return db.query(Status).filter(Status.id == status_id).first()


def get_statuses(db: Session):
    return db.query(Status).all()


def update_status(db: Session, status_id: int, status: StatusCreate):
    db_status = db.query(Status).filter(Status.id == status_id).first()
    if not db_status:
        return None

    db_status.name = status.name
    db.commit()
    db.refresh(db_status)
    return db_status


def delete_status(db: Session, status_id: int):
    db_status = db.query(Status).filter(Status.id == status_id).first()
    if not db_status:
        return None

    db.delete(db_status)
    db.commit()
    return db_status
