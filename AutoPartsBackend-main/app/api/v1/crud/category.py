from sqlalchemy.orm import Session
from app.api.v1.models import category as model
from app.api.v1.schemas import category as schema

def create_category(db: Session, category: schema.CategoryCreate):
    db_category = model.Category(
        name=category.name
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(model.Category).filter(model.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, category: schema.CategoryCreate):
    db_category = db.query(model.Category).filter(model.Category.id == category_id).first()
    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)
        return db_category
    return None

def delete_category(db: Session, category_id: int):
    db_category = db.query(model.Category).filter(model.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category
    return None
