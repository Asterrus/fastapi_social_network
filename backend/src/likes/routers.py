from fastapi import APIRouter, Depends, status, HTTPException
from likes.likes_manager import get_redis_like_manager, RedisLikeManager
from likes.schemas import Like
from posts.post_manager import PostManager, get_post_manager
from users.models import User
from users.user_manager import current_active_user

likes_router = APIRouter(
    prefix='/posts',
    tags=["posts"],
)


@likes_router.get('/{id}/like', status_code=status.HTTP_200_OK, response_model=Like)
async def like(
        id: int,
        user: User = Depends(current_active_user),
        post_manager: PostManager = Depends(get_post_manager),
        like_manager: RedisLikeManager = Depends(get_redis_like_manager)
):
    post = await post_manager.get(id)
    if post.author_id == user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You can not like your post')
    return await like_manager.like(post.id, user.id)


@likes_router.get('/{id}/likes_count', status_code=status.HTTP_200_OK)
async def likes_count(
        id: int,
        post_manager: PostManager = Depends(get_post_manager),
        like_manager: RedisLikeManager = Depends(get_redis_like_manager)
):
    post = await post_manager.get(id)
    return await like_manager.likes_count(post.id)
