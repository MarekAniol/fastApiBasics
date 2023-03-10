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
    
    name: Optional[str] = Field(description="Item name")
    price: Optional[float] = Field(description="Item price in dolars")
    count: Optional[int] = Field(description="Amount of item in stock")
    id: Optional[int] = Field(description="Unique integer specified for item")
    category: Optional[Category] = Field(description="Item category")
    