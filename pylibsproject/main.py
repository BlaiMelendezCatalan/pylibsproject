from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union, List


app = FastAPI()


class Item(BaseModel):
    name: str
    price: Union[int, float]


items = []
items.append(Item(name='Apple', price='0.25'))
items.append(Item(name='Orange', price='0.3'))
items.append(Item(name='Banana', price='0.2'))


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
    return items[offset: limit]


@app.put("/items/")
def create_item(item_id: int, item: Item) -> None:
    items.insert(item_id, item)
