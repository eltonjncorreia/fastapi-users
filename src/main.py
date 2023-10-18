from fastapi import Depends
from fastapi import FastAPI
from fastapi import status
from sqlalchemy.orm import Session

from src.database import get_session
from src.users.repository import UserRepository
from src.users.schemas import UserCreate
from src.users.schemas import UserCreateResponse

app = FastAPI()


@app.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserCreateResponse,  # noqa: E501
)
def create_users(
    user: UserCreate, session: Session = Depends(get_session)  # noqa: B008
):
    user_model = UserRepository(session).create(user)
    return user_model
