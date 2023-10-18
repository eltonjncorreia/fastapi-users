from datetime import datetime

from src.users.models import Claim
from src.users.models import Role
from src.users.models import User


def test_create_role(session, role: Role) -> None:
    retrieved_role = session.query(Role).one()

    assert retrieved_role.description == "Admin"


def test_create_claim(session) -> None:
    claim = Claim(description="Edit Content", active=True)
    session.add(claim)
    session.commit()

    retrieved_claim = session.query(Claim).one()

    assert retrieved_claim.description == "Edit Content"
    assert retrieved_claim.active


def test_create_user(session, role: Role) -> None:
    user = User(
        name="Elton Correia",
        email="elton@example.com",
        password="password",
        role=role,
        created_at=datetime.now(),
    )
    session.add(user)
    session.commit()

    retrieved_user = session.query(User).first()

    assert retrieved_user.name == user.name
    assert retrieved_user.email == user.email
    assert retrieved_user.role == role
