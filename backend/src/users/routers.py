from fastapi import APIRouter

from .schemas import UserRead, UserUpdate

from .user_manager import fastapi_users

users_router = APIRouter()

users_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
