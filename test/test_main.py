from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_signup():
    # signup
    response = client.post(
        "/signup",
        json={"username": "testuser", "email": "test@exmaple.com", "password": "testpass"}

    )
    assert response.status_code == 201
    data = response.json()
    assert "username" in data
    assert data["username"] == "testuser"


def test_login():
    # login
    response = client.post(
        "/token",
        data={"username": "testuser", "password": "testpass"},
        headers={"Content-type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
