from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)



def test_register():

    response = client.post(
        "/api/auth/register",
        params={
            "email":"integration2@gmail.com",
            "password":"123456"
        }
    )


    assert response.status_code in [200,201]



def test_login():

    response = client.post(
        "/api/auth/login",
        params={
            "email":"integration@gmail.com",
            "password":"123456"
        }
    )


    assert response.status_code == 200

    assert "access_token" in response.json()