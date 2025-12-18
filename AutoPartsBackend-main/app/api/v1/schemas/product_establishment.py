from pydantic import BaseModel

class ProductEstablishmentBase(BaseModel):
    establishment_id: int
    product_id: int

class ProductEstablishmentCreate(ProductEstablishmentBase):
    pass

class ProductEstablishment(ProductEstablishmentBase):
    id: int
    establishment_id: int
    product_id: int

    class Config:
        orm_mode = True
