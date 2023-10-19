from src.users.models import Claim
from src.users.models import Role
from src.users.models import User
from src.users.models import UserClaim
from src.users.schemas import UserCreate


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, user_create: UserCreate) -> User:
        try:
            role = Role(description=user_create.role.description)
            self.session.add(role)

            user = User(
                name=user_create.name,
                email=user_create.email,
                password=user_create.password,
                role=role,
                created_at=user_create.created_at,
                updated_at=user_create.updated_at,
            )
            self.session.add(user)

            for claim_data in user_create.claims:
                claim = Claim(
                    description=claim_data.description,
                    active=claim_data.active,
                )
                self.session.add(claim)
                self.session.flush()

                user_claim = UserClaim(user_id=user.id, claim_id=claim.id)
                self.session.add(user_claim)

            self.session.commit()

            return user

        except Exception as e:
            self.session.rollback()
            raise e
