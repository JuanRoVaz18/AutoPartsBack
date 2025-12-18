from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class ShoppingCartProduct(Base):
    __tablename__ = 'shopping_cart_products'

    id = Column(Integer, primary_key=True, index=True)
    shopping_cart_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)
