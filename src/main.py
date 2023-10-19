from fastapi import Depends
from fastapi import FastAPI
from fastapi import status
from sqlalchemy.orm import Session

from src.database import get_session
from src.users.repositories import UserRepository
from src.users.schemas import ClaimCreateResponse
from src.users.schemas import RoleCreateResponse
from src.users.schemas import UserCreate
from src.users.schemas import UserCreateResponse

app = FastAPI()


@app.post(
    "/users/", status_code=status.HTTP_201_CREATED, response_model=UserCreateResponse
)
def create_users(user: UserCreate, session: Session = Depends(get_session)):
    user_created = UserRepository(session).create(user)
    user_response = UserCreateResponse(
        id=user_created.id,
        name=user_created.name,
        email=user_created.email,
        role_id=user_created.role_id,
        created_at=user_created.created_at.isoformat(),
        updated_at=user_created.updated_at.isoformat(),
        role=RoleCreateResponse(
            id=user_created.role.id, description=user_created.role.description
        ),
        claims=[
            ClaimCreateResponse(id=c.id, description=c.description, active=c.active)
            for c in user_created.claims
        ],
    )
    return user_response
