import sys
sys.path.append('../')
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class Category(Enum):
    """Category of an item"""
    
    TOOLS = "tools"
    CONSUMABLES = "consumables"
    TOYS = "toys"


class Item(BaseModel):
    """Item api model representation"""

    id: Optional[int] = Field(description="Unique integer specified for item")    
    name: Optional[str] = Field(description="Item name")
    description: Optional[str] = Field(description="Item description")
    price: Optional[float] = Field(description="Item price in dolars")
    count: Optional[int] = Field(description="Amount of item in stock")
    category: Optional[Category] = Field(description="Item category")
    is_in_stock: Optional[bool] = Field(description="Is item available in stock")
    
    class Config:
        orm_mode=True
    