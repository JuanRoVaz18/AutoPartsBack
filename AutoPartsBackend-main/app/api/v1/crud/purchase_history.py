from sqlalchemy.orm import Session
from app.api.v1.models import purchase_history as model
from app.api.v1.schemas import purchase_history as schema

def create_purchase_history(db: Session, data: schema.PurchaseHistoryCreate):
    obj = model.PurchaseHistory(
        name=data.name,
        purchase_date=data.purchase_date,
        order_id=data.order_id
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_purchase_history(db: Session, history_id: int):
    return db.query(model.PurchaseHistory).filter(
        model.PurchaseHistory.id == history_id
    ).first()

def get_purchase_histories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.PurchaseHistory).offset(skip).limit(limit).all()

def delete_purchase_history(db: Session, history_id: int):
    obj = db.query(model.PurchaseHistory).filter(
        model.PurchaseHistory.id == history_id
    ).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
