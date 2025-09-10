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
        json={"username": "testuser", "email": "test@example.com", "password": "testpass"}

    )
    assert response.status_code in (201, 400)
    data = response.json()
    if response.status_code == 201:
        # Success → should return user info (username, email, etc.)
        assert "username" in data
        assert data["username"] == "testuser"
    else:
        # Failure → user already exists
        assert data["detail"] == "username or email already registered"


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


def test_access_me():
    # 1. login to get token
    login_resp = client.post(
        "/token",
        data={"username": "testuser", "password": "testpass"},
        headers={"Content-type": "application/x-www-form-urlencoded"}
    )
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]

    # 2. use token to access /me
    me_resp = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert me_resp.status_code == 200
    data = me_resp.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
