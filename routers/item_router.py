from fastapi import APIRouter, HTTPException, Path, Query
from domain_models.item_model import Item, Category


router = APIRouter()


items = {
    0: Item(name="Milk", price=6.55, count=2, id=0, category=Category.CONSUMABLES),
    1: Item(name="Juice", price=5.99, count=3, id=1, category=Category.CONSUMABLES),
    2: Item(name="Brush", price=8.90, count=1, id=2, category=Category.TOOLS),
}


@router.get("/items")
def get_all_items() -> dict[str, dict[int, Item]]:
    return {"items": items}

@router.get("/items/{item_id}")
def query_item_by_id(item_id: int = Path(ge=0)) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id} id does not exist"
        )
    return items[item_id]

@router.get("/selected/items", response_model=None)
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, any]:
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category == category,
            )
        )
    selection_items = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection_items,
    }

@router.post("/items")
def add_item(item: Item) -> dict[str, Item]:
    
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with {item.id=} already exist")
    
    items[item.id] = item
    return {"added": item}

@router.delete("/items/{item_id}")
def del_item_by_id(item_id: int) -> dict[str, Item]:
    
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail=f"Idem with {item_id=} does not exist",
        )
    
    item = items.pop(item_id)
    return {"deleted": item}

@router.put("/items/{item_id}")
def update_item(
    item_id: int | None = Query(default=None, gt=0),
    name: str | None = Query(default=None,  min_length=1, max_length=10),
    price: float | None = Query(default=None, gt=0.0),
    count: int | None = Query(default=None, ge=0)
    ):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    if all(item_data is None for item_data in (name, price, count)):
        raise HTTPException(status_code=400, detail="No parameters provided for update item")
    
    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count
        
    return {"updated": item}