"""Define the Item class."""
from typing import Optional, Union

from pydantic import BaseModel


class Item(BaseModel):
    """Store the name and price of an item.

    Parameters
    ----------
    name : str
        The name of the item.
    price : int
        The price of the item.
    available : bool
        Whether or not the item is available

    Examples
    --------
    Create an item with name "Apple" and price 0.25.

    >>> from pylibsproject import Item
    >>> item = Item(name="Apple", price=0.25)
    >>> item
    Item(name='Apple', price=0.25)

    """

    name: str
    price: Union[int, float]
    available: Optional[bool] = True
