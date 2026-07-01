from pymongo import MongoClient
from config import mongouri

client = MongoClient(mongouri)

# Database name
db = client["fastapi_db"]

# Collection
items_collection = db["items"]
users_collection = db["users"]
