from fastapi import status

from src.users.models import User


def test_create_user(client, session, payload_create_user, response_create_user):
    response = client.post("/users/", json=payload_create_user)
    payload_create_user.pop("password")

    user = session.query(User).filter_by(id=response.json().get("id")).one()

    response_expected = {
        "id": user.id,
        "name": "Elton Correia",
        "email": "elton@example.com",
        "role_id": user.role.id,
        "created_at": "2023-10-18",
        "updated_at": "2023-10-19",
        "role": {"id": user.role.id, "description": "Moderator"},
        "claims": response.json()["claims"],
    }

    assert response.json() == response_expected
    assert response.status_code == status.HTTP_201_CREATED
