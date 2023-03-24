from fastapi import APIRouter, HTTPException, Path, Query, status
from fastapi.encoders import jsonable_encoder
from item_model import Item
from sqlalchemy.future import select
from database import get_session
from typing import List
import db_models


router = APIRouter()
async_session = get_session()

async def get_db():
    async with async_session() as session:
        yield session

async def load_items():
    try:
        async with async_session() as session:
            stmt = select(db_models.Item)
            result = await session.execute(stmt)
            items = result.scalars().all()
        return items
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error loading items from database",
            )

@router.get("/items", response_model=List[Item], status_code=200)
async def get_all_items() -> List[Item]:
    items = await load_items()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")
    return items

@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> dict[str, Item]:
    
    new_item = db_models.Item(
        id=item.id,
        name=item.name,
        price=item.price,
        count=item.count,
        description=item.description,
        is_in_stock=item.is_in_stock
    )
    
    async with async_session() as db:
        try:
            db.add(new_item)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    return new_item
