# FastAPI CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with **FastAPI** and **MongoDB** using **PyMongo**.

## Features

* FastAPI backend
* MongoDB database
* CRUD Operations
* RESTful API
* Ready for deployment on Render

---

# Tech Stack

* Python 3.x
* FastAPI
* PyMongo
* MongoDB Atlas / Local MongoDB
* Uvicorn

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create `.env`

Create a `.env` file in the project root.

```env
MONGO_URI=your_mongodb_connection_string
```

Example

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

# Run the Server

```bash
uvicorn app:app --reload
```

Server starts at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Database

Database Name

```
fastapi_db
```

Collection

```
items
```

---

# API Endpoints

---

## Home

### GET /

Returns a welcome message.

### Request

```
GET /
```

### Response

```json
{
    "message": "FastAPI CRUD is running 🚀"
}
```

---

## Get All Items

### GET /items

Returns every item stored in MongoDB.

### Request

```
GET /items
```

### Example Response

```json
[
    {
        "id": "68618fe13c2d713ce7e40fa7",
        "name": "Laptop",
        "description": "Gaming Laptop",
        "price": 89999
    },
    {
        "id": "68618ff63c2d713ce7e40fa8",
        "name": "Phone",
        "description": "Android Phone",
        "price": 24999
    }
]
```

---

## Get Single Item

### GET /items/{item_id}

Returns a single item by its MongoDB ObjectId.

### Request

```
GET /items/68618fe13c2d713ce7e40fa7
```

### Success Response

```json
{
    "id": "68618fe13c2d713ce7e40fa7",
    "name": "Laptop",
    "description": "Gaming Laptop",
    "price": 89999
}
```

### Error Response

```json
{
    "detail": "Item not found"
}
```

---

## Create Item

### POST /items

Creates a new item.

### Request Body

```json
{
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 3999
}
```

### Response

```json
{
    "id": "6861912b3c2d713ce7e40fab",
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 3999
}
```

---

## Update Item

### PUT /items/{item_id}

Updates an existing item.

### Request

```
PUT /items/68618fe13c2d713ce7e40fa7
```

### Request Body

```json
{
    "name": "Gaming Laptop",
    "description": "RTX 5090 Laptop",
    "price": 149999
}
```

### Success Response

```json
{
    "id": "68618fe13c2d713ce7e40fa7",
    "name": "Gaming Laptop",
    "description": "RTX 5090 Laptop",
    "price": 149999
}
```

### Error Response

```json
{
    "detail": "Item not found"
}
```

---

## Delete Item

### DELETE /items/{item_id}

Deletes an item from MongoDB.

### Request

```
DELETE /items/68618fe13c2d713ce7e40fa7
```

### Success Response

```json
{
    "message": "deleted successfully"
}
```

### Error Response

```json
{
    "detail": "Item not found"
}
```

---

# Item Schema

```json
{
    "name": "string",
    "description": "string",
    "price": 0.0
}
```

---

# Project Structure

```
project/
│
├── app.py
├── database.py
├── config.py
├── requirements.txt
├── .env
├── README.md
└── __pycache__/
```

---

# Environment Variables

| Variable  | Description               |
| --------- | ------------------------- |
| MONGO_URI | MongoDB Connection String |

---

# Example cURL Requests

## Create

```bash
curl -X POST http://127.0.0.1:8000/items \
-H "Content-Type: application/json" \
-d "{\"name\":\"Laptop\",\"description\":\"Gaming Laptop\",\"price\":89999}"
```

## Read All

```bash
curl http://127.0.0.1:8000/items
```

## Read One

```bash
curl http://127.0.0.1:8000/items/<item_id>
```

## Update

```bash
curl -X PUT http://127.0.0.1:8000/items/<item_id> \
-H "Content-Type: application/json" \
-d "{\"name\":\"Updated Laptop\",\"description\":\"Updated Description\",\"price\":99999}"
```

## Delete

```bash
curl -X DELETE http://127.0.0.1:8000/items/<item_id>
```

---

# Notes

* MongoDB automatically generates an `_id` for every document.
* The API converts MongoDB's `_id` into an `id` string before returning responses.
* Use a valid MongoDB ObjectId when requesting, updating, or deleting an item.
* Interactive API documentation is available at `/docs`.

---

# License

This project is provided for learning and demonstration purposes.
