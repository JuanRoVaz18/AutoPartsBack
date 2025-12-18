from pydantic import BaseModel

class ShoppingCartProductBase(BaseModel):
    shopping_cart_id: int
    product_id: int

class ShoppingCartProductCreate(ShoppingCartProductBase):
    pass

class ShoppingCartProduct(ShoppingCartProductBase):
    id: int

    class Config:
        orm_mode = True
