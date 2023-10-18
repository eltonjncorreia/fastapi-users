from src.users.models import Claim
from src.users.models import Role
from src.users.models import User
from src.users.models import UserClaim
from src.users.schemas import UserCreate


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, user: UserCreate) -> User:
        try:
            role = Role(description=user.role.description)
            self.session.add(role)

            user_model = User(
                name=user.name,
                email=user.email,
                password=user.password,
                role=role,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            self.session.add(user_model)

            for claim_data in user.claims:
                claim = Claim(
                    description=claim_data.description,
                    active=claim_data.active,
                )
                self.session.add(claim)
                user_claim = UserClaim(user_id=user_model, claim_id=claim)
                self.session.add(user_claim)

            self.session.commit()

            return user_model

        except Exception as e:
            self.session.rollback()
            raise e
