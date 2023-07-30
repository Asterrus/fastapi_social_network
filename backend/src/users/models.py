from typing import TYPE_CHECKING

from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable

from datetime import datetime, date

from database import Base

if TYPE_CHECKING:
    from posts.models import Post


class User(SQLAlchemyBaseUserTable[int], Base):
    register_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=datetime.utcnow)
    birthdate: Mapped[date | None]
    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))

    posts: Mapped[list["Post"] | None] = relationship(
        back_populates='author', cascade='all, delete-orphan', lazy='selectin',
    )
