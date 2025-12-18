from sqlalchemy import Column, Integer
from app.core.database import Base

class ProductEstablishment(Base):
    __tablename__ = 'product_establishments'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    establishment_id = Column(Integer)
