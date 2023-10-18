from fastapi import status


def test_create_user(client, payload_create_user):
    response = client.post("/users/", json=payload_create_user)
    payload_create_user.pop("password")

    assert response.json() == payload_create_user
    assert response.status_code == status.HTTP_201_CREATED
