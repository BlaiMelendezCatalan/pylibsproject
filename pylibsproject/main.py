"""API to interact with the items."""
from typing import List

from fastapi import FastAPI, HTTPException

from .item import Item

app = FastAPI()


items = []


@app.get("/")
def root() -> dict:
    """Api's root endpoint. Does nothing.

    Returns
    -------
        default dict : dict

    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    """Get an Item given its id.

    Parameters
    ----------
        item_id : int
            id of the item to get

    Returns
    -------
        Item : Item
            Item object with id item_id

    """
    if item_id >= len(items):
        return HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.get("/items/")
def list_items(offset: int, limit: int = 10) -> List[Item]:
    """List a number of items.

    Parameters
    ----------
        offset : int
            position to start listing from
        limit : int
            position to stop listing at

    Returns
    -------
        List[Item] : List[Item]
            A list of Item objects

    """
    return items[offset:limit]


@app.put("/items/")
def create_item(item: Item) -> None:
    """Create a new item.

    Parameters
    ----------
        item : Item
            Item to create

    """
    items.append(item)
