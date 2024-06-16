from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from .user import UserDAO


class HolderDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.user = UserDAO(session)

    async def commit(self) -> None:
        await self._session.commit()
