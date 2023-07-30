from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class PostRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    title: str
    content: str
    author_id: int


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=2000)


class PostUpdate(BaseModel):
    title: str | None = Field(min_length=1, max_length=100, default=None)
    content: str | None = Field(min_length=1, max_length=2000, default=None)
