from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin, FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_config import auth_backend
from config import SECRET
from .models import User
from database import get_async_session
from .user_databse import CustomSQLAlchemyUserDatabase


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield CustomSQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
