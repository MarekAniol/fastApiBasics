from database import Base
from sqlalchemy import Column, String, Float, Integer, Enum, Text, Boolean
from item_model import Category


class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)  
    count = Column(Integer)   
    category = Column(Enum(Category))
    is_in_stock = Column(Boolean, nullable=False)
    
    
    def __repr__(self) -> str:
        return super().__repr__()