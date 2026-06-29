from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Basic FastAPI CRUD",
    version="1.0.0",
    description="Simple CRUD example for deployment on Render"
)


# -----------------------------
# Model
# -----------------------------

class Item(BaseModel):
    name: str
    description: str
    price: float


class ItemResponse(Item):
    id: int


# -----------------------------
# Fake Database
# -----------------------------

db = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "Gaming Laptop",
        "price": 999.99,
    },
    {
        "id": 2,
        "name": "Mouse",
        "description": "Wireless Mouse",
        "price": 25.50,
    },
]

next_id = 3


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI CRUD is running 🚀"
    }


# -----------------------------
# Read All
# -----------------------------

@app.get("/items", response_model=List[ItemResponse])
def get_items():
    return db


# -----------------------------
# Read One
# -----------------------------

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):

    for item in db:
        if item["id"] == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")


# -----------------------------
# Create
# -----------------------------

@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: Item):

    global next_id

    new_item = {
        "id": next_id,
        **item.model_dump()
    }

    db.append(new_item)
    next_id += 1

    return new_item


# -----------------------------
# Update
# -----------------------------

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated: Item):

    for item in db:

        if item["id"] == item_id:

            item["name"] = updated.name
            item["description"] = updated.description
            item["price"] = updated.price

            return item

    raise HTTPException(status_code=404, detail="Item not found")


# -----------------------------
# Delete
# -----------------------------

@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    for index, item in enumerate(db):

        if item["id"] == item_id:
            db.pop(index)

            return {
                "message": "Item deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Item not found")