from typing import List
from typing import Optional

from pydantic import BaseModel


class RoleCreate(BaseModel):
    description: str


class ClaimCreate(BaseModel):
    description: Optional[str] = None
    active: bool = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: Optional[str] = None
    role_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    role: RoleCreate
    claims: List[ClaimCreate]


class RoleCreateResponse(BaseModel):
    id: int
    description: str


class ClaimCreateResponse(BaseModel):
    id: int
    description: str
    active: bool


class UserCreateResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str
    role_id: int
    created_at: str
    updated_at: str
    role: RoleCreateResponse
    claims: List[ClaimCreateResponse]
