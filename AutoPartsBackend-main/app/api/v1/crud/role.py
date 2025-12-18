from sqlalchemy.orm import Session
from app.api.v1.models.role import Role
from app.api.v1.schemas.role import RoleCreate


def create_role(db: Session, role: RoleCreate):
    db_role = Role(
        name=role.name,
        description=role.description
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Role).offset(skip).limit(limit).all()


def update_role(db: Session, role_id: int, role: RoleCreate):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return None

    db_role.name = role.name
    db_role.description = role.description
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(db: Session, role_id: int):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return None

    db.delete(db_role)
    db.commit()
    return db_role
