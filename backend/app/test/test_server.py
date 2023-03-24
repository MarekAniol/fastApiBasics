import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests


print("-------------------------------------")
print("Get all items")
print(requests.get('http://127.0.0.1:8000/items').json())
print("-------------------------------------")
print("Get item by query parameters")
print(requests.get('http://127.0.0.1:8000/selected/items?name=Milk').json())
print("-------------------------------------")
print("Post item")
print(requests.post(
    'http://127.0.0.1:8000/items',
        json={
            "name": "Yellow car toy",
            "price": 12.99, "count": 14,
            "id": 5,
            "category": "toys"
            }
        ).json()
      )
print("-------------------------------------")
print("Delete item")
print(requests.delete('http://127.0.0.1:8000/items/3').json())
print("-------------------------------------")
print("Get all items")
print(requests.get('http://127.0.0.1:8000/items').json())
print("-------------------------------------")
print("Update item")
print(requests.put('http://127.0.0.1:8000/items/0?count=800').json())
