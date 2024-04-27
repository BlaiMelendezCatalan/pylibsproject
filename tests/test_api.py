import os

import pytest
import requests

from pylibsproject import Item

ENDPOINT = "http://127.0.0.1:8000/"


def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.parametrize("name,price,available", [("Apple", 0.25, True)])
def test_create_item(name: str, price: float, available: bool):
    item = Item(name=name, price=price)
    endpoint_put = os.path.join(ENDPOINT, "items")
    response_put = requests.put(endpoint_put, json=dict(item))
    endpoint_get = os.path.join(ENDPOINT, "items", "0")
    response_get = requests.get(endpoint_get)
    exp_get_response = {"name": name, "price": price, "available": available}

    assert response_put.status_code == 200
    assert response_get.status_code == 200
    assert response_get.json() == exp_get_response
