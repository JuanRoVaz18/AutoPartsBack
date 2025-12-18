from pydantic import BaseModel


class ProductImageBase(BaseModel):
    product_id: int
    image_id: int


class ProductImageCreate(ProductImageBase):
    pass


class ProductImage(ProductImageBase):
    class Config:
        orm_mode = True
