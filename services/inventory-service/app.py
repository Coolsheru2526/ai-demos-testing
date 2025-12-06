from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inventory Service")

# Fake in-memory database
inventory_db = {
    "item_001": {"name": "Keyboard", "quantity": 12},
    "item_002": {"name": "Mouse", "quantity": 30},
    "item_003": {"name": "Laptop", "quantity": 5},
}


class UpdateItem(BaseModel):
    quantity: int


@app.get("/")
def root():
    return {"service": "inventory-service", "status": "running"}


@app.get("/inventory")
def get_all_inventory():
    return inventory_db


@app.get("/inventory/{item_id}")
def get_item(item_id: str):
    if item_id not in inventory_db:
        return {"error": "Item not found"}
    return inventory_db[item_id]


@app.post("/inventory/{item_id}")
def update_item(item_id: str, data: UpdateItem):
    if item_id not in inventory_db:
        return {"error": "Item not found"}

    inventory_db[item_id]["quantity"] = data.quantity
    return {
        "message": "Quantity updated",
        "item_id": item_id,
        "new_quantity": data.quantity
    }


@app.post("/inventory/add/{item_id}")
def add_new_item(item_id: str, name: str, quantity: int = 0):
    if item_id in inventory_db:
        return {"error": "Item already exists"}

    inventory_db[item_id] = {"name": name, "quantity": quantity}
    return {"message": "Item added", "item": inventory_db[item_id]}
