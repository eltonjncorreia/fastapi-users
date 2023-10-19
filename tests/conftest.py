from typing import Dict

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings
from src.main import app
from src.users.models import Base
from src.users.models import Role


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine(settings.DATABASE_URL)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def role(session) -> Role:
    role = Role(description="Admin")
    session.add(role)
    session.commit()
    return role


@pytest.fixture
def payload_create_user() -> Dict:
    return {
        "name": "Elton Correia",
        "email": "elton@example.com",
        "password": "hashed_password",
        "role_id": 2,
        "created_at": "2023-10-18",
        "updated_at": "2023-10-19",
        "role": {"description": "Moderator"},
        "claims": [{"description": "Claim A", "active": True}],
    }


@pytest.fixture
def response_create_user() -> Dict:
    return {
        "id": 23,
        "name": "Elton Correia",
        "email": "elton@example.com",
        "role_id": 59,
        "created_at": "2023-10-18",
        "updated_at": "2023-10-19",
        "role": {"id": 59, "description": "Moderator"},
        "claims": [{"id": 59, "description": "Claim A", "active": True}],
    }
