from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy as sa

from .base import BaseModel, TimestampMixin
from src.infra import dto


class User(BaseModel, TimestampMixin):
    id: Mapped[int] = mapped_column(sa.BIGINT, primary_key=True)
    username: Mapped[str] = mapped_column(sa.VARCHAR(33))

    def to_dto(self) -> dto.UserDTO:
        return dto.UserDTO(
            id=self.id,
            username=self.username,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
