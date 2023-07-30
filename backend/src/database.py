from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (async_sessionmaker,
                                    create_async_engine, AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = (f"postgresql+asyncpg://{DB_USER}:{DB_PASS}"
                f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator:
    async with async_session_maker() as session:
        yield session


class Base(AsyncAttrs, DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
