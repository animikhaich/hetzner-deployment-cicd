from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the FastAPI test app! - Combine Build & Deploy"
    }


def test_read_item_without_query():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "query": None}


def test_read_item_with_query():
    response = client.get("/items/2?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2, "query": "testquery"}


def test_create_item():
    item_data = {"name": "test", "price": 10}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"item": item_data, "status": "created"}


def test_create_item_empty():
    response = client.post("/items/", json={})
    assert response.status_code == 200
    assert response.json() == {"item": {}, "status": "created"}


def test_update_item():
    item_data = {"name": "updated", "price": 20}
    response_json = {"item_id": 1, "item": item_data, "status": "updated"}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 200
    assert response.json() == response_json


def test_update_item_empty():
    response = client.put("/items/2", json={})
    assert response.status_code == 200
    assert response.json() == {"item_id": 2, "item": {}, "status": "updated"}


def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "status": "deleted"}


def test_delete_item_with_non_int_id():
    response = client.delete("/items/notanint")
    assert response.status_code == 422  # FastAPI validation error


def test_read_item_with_non_int_id():
    response = client.get("/items/notanint")
    assert response.status_code == 422


def test_update_item_with_non_int_id():
    response = client.put("/items/notanint", json={"name": "fail"})
    assert response.status_code == 422
