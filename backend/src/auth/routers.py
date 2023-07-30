from fastapi import APIRouter
from auth.auth_config import auth_backend
from users.routers import fastapi_users
from users.schemas import UserRead, UserCreate

auth_router = APIRouter()

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

