from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return await self.session.scalar(statement)

    async def get_by_id(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)

    async def create(
        self,
        username: str,
        email: str,
        password_hash: str,
    ) -> User:
        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
