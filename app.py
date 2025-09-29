from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI test app! - Combine Build & Deploy"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


@app.post("/items/")
def create_item(item: dict):
    return {"item": item, "status": "created"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item, "status": "updated"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "status": "deleted"}
