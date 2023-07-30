from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from posts.models import Post
from posts.schemas import PostCreate, PostUpdate
from users.models import User


class PostManager:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = Post

    async def get(self, id: int) -> Post:
        stmt = select(self.model).where(self.model.id == id)
        post = await self.session.scalar(stmt)
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} not exists')

        return post

    async def create(self, post_create: PostCreate, author: User) -> Post:
        new_post = Post(**post_create.model_dump())
        new_post.author = author
        self.session.add(new_post)
        await self.session.commit()
        return new_post

    async def update(self, id: int, post_update: PostUpdate, updated_by: User) -> Post:
        post = await self.get(id)
        if post.author_id != updated_by.id and not updated_by.is_superuser:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You can not update this post')

        update_data = post_update.model_dump(exclude_unset=True, exclude_defaults=True)
        for key, value in update_data.items():
            setattr(post, key, value)

        await self.session.commit()
        return post

    async def delete(self, id: int, deleted_by: User):
        post = await self.get(id)
        if post.author_id != deleted_by.id and not deleted_by.is_superuser:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You can not delete this post')
        await self.session.delete(post)
        await self.session.commit()


async def get_post_manager(session=Depends(get_async_session)):
    yield PostManager(session)
