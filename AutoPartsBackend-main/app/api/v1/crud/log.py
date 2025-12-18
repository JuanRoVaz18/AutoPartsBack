from sqlalchemy.orm import Session
from app.api.v1.models import log as model
from app.api.v1.schemas import log as schema

def create_log(db: Session, log: schema.LogCreate):
    db_log = model.Log(action=log.action)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_log(db: Session, log_id: int):
    return db.query(model.Log).filter(model.Log.id == log_id).first()

def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Log).offset(skip).limit(limit).all()

def update_log(db: Session, log_id: int, log: schema.LogCreate):
    db_log = db.query(model.Log).filter(model.Log.id == log_id).first()
    if not db_log:
        return None

    db_log.action = log.action
    db.commit()
    db.refresh(db_log)
    return db_log

def delete_log(db: Session, log_id: int):
    db_log = db.query(model.Log).filter(model.Log.id == log_id).first()
    if not db_log:
        return None

    db.delete(db_log)
    db.commit()
    return db_log
