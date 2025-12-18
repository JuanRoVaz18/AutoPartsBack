from sqlalchemy.orm import Session
from app.api.v1.models import user as model
from app.api.v1.schemas import user as schema

def create_user(db: Session, user: schema.UserCreate):
    db_user = model.User(
        name=user.name,
        email=user.email,
        password=user.password,  # luego se puede hashear
        phone=user.phone,
        birthday=user.birthday,
        document_id=user.document_id,
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: schema.UserCreate):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if not db_user:
        return None

    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db_user.phone = user.phone
    db_user.birthday = user.birthday
    db_user.document_id = user.document_id
    db_user.role_id = user.role_id

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
