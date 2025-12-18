from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.v1.crud import role as crud
from app.api.v1.schemas.role import Role, RoleCreate
from app.core.database import get_db

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.post("/", response_model=Role)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db, role)


@router.get("/", response_model=List[Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_roles(db, skip, limit)


@router.get("/{role_id}", response_model=Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.get_role(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role


@router.put("/{role_id}", response_model=Role)
def update_role(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    db_role = crud.update_role(db, role_id, role)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role


@router.delete("/{role_id}", response_model=Role)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.delete_role(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
