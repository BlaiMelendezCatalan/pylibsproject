from typing import List

from fastapi import FastAPI, HTTPException

from .item import Item

app = FastAPI()


items = []


@app.get("/")
def root() -> dict:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id >= len(items):
        return HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.get("/items/")
def list_items(offset: int, limit: int = 10) -> List[Item]:
    return items[offset:limit]


@app.put("/items/")
def create_item(item: Item) -> None:
    items.append(item)
