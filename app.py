from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import items_collection
from bson import ObjectId
from routes.auth import router as auth_router


app = FastAPI()

app.include_router(auth_router)


def serialize_item(item):
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "price": item["price"]
    }

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

@app.get("/items")
def get_items():
    items = items_collection.find()

    return [
        serialize_item(item)
        for item in items
    ]


# -----------------------------
# Read One
# -----------------------------

@app.get("/items/{item_id}")
def get_item(item_id: str):

    item = items_collection.find_one(
        {"_id": ObjectId(item_id)}
    )

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return serialize_item(item)


# -----------------------------
# Create
# -----------------------------

@app.post("/items")
def create_item(item: Item):
    result = items_collection.insert_one(item.model_dump())

    new_item = items_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_item(new_item)


# -----------------------------
# Update
# -----------------------------

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, updated: Item):
    result = items_collection.find_one(
        {"_id": ObjectId(item_id)},
        {
            "$set": updated.model_dump()
        }
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404, detail="Item not found"
        )

    item = items_collection.find_one({
        "_id": ObjectId(item_id)
    })

    return item


# -----------------------------
# Delete
# -----------------------------

@app.delete("/items/{item_id}")
def delete_item(item_id: str):

    result = items_collection.delete_one({
        "_id": ObjectId(item_id)
    })

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "deleted successfully"}
