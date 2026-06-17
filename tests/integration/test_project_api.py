from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)



def login():

    response = client.post(
        "/api/auth/login",
        params={
            "email":"integration@gmail.com",
            "password":"123456"
        }
    )

    return response.json()["access_token"]



def test_create_project():

    token = login()


    response = client.post(
        "/api/projects",
        headers={
            "Authorization": f"Bearer {token}"
        },
        params={
            "name": "Integration Project",
            "description": "API test"
        }
)


    assert response.status_code == 200


def test_get_projects():

    token = login()


    response = client.get(
        "/api/projects",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )


    assert response.status_code == 200