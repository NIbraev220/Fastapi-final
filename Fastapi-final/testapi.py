from fastapi.testclient import TestClient


client = TestClient(app)


def sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {{"result": 55}}

def fibo():
    response = client.get("/fibo")
    assert response.status_code == 200
    assert response.json() == {{"result": 3}}

def reverse():
    response = client.post("/reverse", {"string: hello"})
    assert response.status_code == 200
    assert response.json() == {{"result": "olleh"}}

def list():
    response = client.put("/list", {"element":"Apple"})
    assert response.status_code == 200
    assert response.json() =={{"result": "Apple"}}

def calculator():
    response = client.post("/calculator", {{"expr": "1,+,1"}})
    assert response.status_code == 200
    assert response.json() =={{"result": 2}}

