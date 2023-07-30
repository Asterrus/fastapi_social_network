from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from users.models import User


class Post(Base):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=datetime.utcnow)
    published: Mapped[bool] = mapped_column(default=False)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(2000))
    author: Mapped["User"] = relationship(back_populates='posts')
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
