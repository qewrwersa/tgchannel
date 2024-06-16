from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra import dto
from src.infra.database.dao.base import BaseDAO
from src.infra.database.models import User


class UserDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_user(self, user_id: int) -> dto.UserDTO | None:
        stmt = select(User).where(User.id == user_id)

        result = await self._session.scalars(stmt)

        user: User = result.first()

        if not user:
            return None

        return user.to_dto()

    async def get_user_by_username(self, username: str) -> dto.UserDTO | None:
        stmt = select(User).where(User.username == username)

        result = await self._session.scalars(stmt)

        user: User = result.first()

        if not user:
            return None

        return user.to_dto()

    async def add_user(self, user_id: int, username: str) -> dto.UserDTO:
        stmt = insert(User).values(id=user_id, username=username).returning(User)

        return (await self._session.scalars(stmt)).first().to_dto()

