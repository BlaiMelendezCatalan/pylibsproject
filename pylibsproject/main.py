"""API to interact with the items."""
import logging
import sys
from typing import List

from fastapi import FastAPI, HTTPException

from .decorators import benchmark
from .item import Item

app = FastAPI()


items = []


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] "
    "[%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


@app.get("/")
@benchmark(logger=logger)
def root() -> dict:
    """Api's root endpoint. Does nothing.

    Returns
    -------
        default dict : dict

    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
@benchmark(logger=logger)
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
@benchmark(logger=logger)
def list_items(offset: int = 0, limit: int = 10) -> List[Item]:
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
@benchmark(logger=logger)
def create_item(item: Item) -> None:
    """Create a new item.

    Parameters
    ----------
        item : Item
            Item to create

    """
    items.append(item)
