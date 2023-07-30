from fastapi import APIRouter, status, Depends

from posts.post_manager import PostManager, get_post_manager
from posts.schemas import PostRead, PostCreate, PostUpdate
from users.models import User
from users.user_manager import current_active_user

post_router = APIRouter(
    prefix='/posts',
    tags=["posts"],
)


@post_router.get(
    path='/{id}',
    response_model=PostRead,
    status_code=status.HTTP_200_OK
)
async def get_post(
        id: int,
        post_manager: PostManager = Depends(get_post_manager),
):
    post = await post_manager.get(id)
    return post


@post_router.post(
    path='/create',
    response_model=PostRead,
    status_code=status.HTTP_201_CREATED
)
async def create_post(
        post_create: PostCreate,
        post_manager: PostManager = Depends(get_post_manager),
        author: User = Depends(current_active_user)
):
    post = await post_manager.create(post_create, author)
    return post


@post_router.patch(
    path='/{id}/update',
    response_model=PostRead,
    status_code=status.HTTP_200_OK
)
async def update_post(
        id: int,
        post_update: PostUpdate,
        post_manager: PostManager = Depends(get_post_manager),
        updated_by: User = Depends(current_active_user)
):
    post = await post_manager.update(id, post_update, updated_by)
    return post


@post_router.delete(
    path='/{id}/delete',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_post(
        id: int,
        post_manager: PostManager = Depends(get_post_manager),
        deleted_by: User = Depends(current_active_user)
):
    await post_manager.delete(id, deleted_by)
