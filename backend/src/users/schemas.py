import asyncio
import concurrent
from datetime import datetime, date
from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationError

from auth.utils import get_email_status
from config import USE_HUNTER_URL


class UserInfoMixin(BaseModel):
    first_name: str | None = Field(min_length=1, max_length=50, default=None)
    last_name: str | None = Field(min_length=1, max_length=50, default=None)
    birthdate: date | None = Field(default=None)

    @field_validator('birthdate')
    def validate_birthdate(cls, value):
        if value > datetime.now().date():
            raise ValueError('birthdate cannot be in the future')
        return value


class UserPosts(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserRead(schemas.BaseUser[int]):
    first_name: str | None
    last_name: str | None
    birthdate: date | None
    register_at: datetime
    updated_at: datetime
    posts: list[UserPosts] | None


class UserCreate(UserInfoMixin, schemas.BaseUserCreate):

    @field_validator('email')
    def validate_email(cls, value):
        if USE_HUNTER_URL == 'True':
            try:
                pool = concurrent.futures.ThreadPoolExecutor(1)
                status = pool.submit(asyncio.run, get_email_status(value)).result()
                if status == 'invalid':
                    raise ValidationError('Invalid Email')
            except Exception:
                pass
        return value


class UserUpdate(UserInfoMixin, schemas.BaseUserUpdate):
    pass
