import redis.asyncio


class RedisLikeManager:
    def __init__(
            self,
            redis: redis.asyncio.Redis,
            lifetime_seconds: int | None = None,
            *,
            key_prefix: str = "fastapi_users_likes:",
    ):
        self.redis = redis
        self.lifetime_seconds = lifetime_seconds
        self.key_prefix = key_prefix

    async def like(
            self,
            post_id: int,
            user_id: int,
    ):
        like_name = f"{self.key_prefix}user_id-{user_id}, post_id-{post_id}"
        like_count_name = f"{self.key_prefix}post_id-{post_id}_likes_count"

        like = await self.redis.get(like_name)

        if like:
            await self.redis.delete(like_name)
            await self.redis.decr(like_count_name, 1)
            return {'data': 'Disliked !'}

        await self.redis.set(like_name, 1, ex=self.lifetime_seconds)
        await self.redis.incr(like_count_name, 1)
        return {'data': 'Liked !'}

    async def likes_count(
            self,
            post_id: int,
    ):
        return await self.redis.get(f"{self.key_prefix}post_id-{post_id}_likes_count")


redis = redis.asyncio.from_url("redis://redis:6379", decode_responses=True)


def get_redis_like_manager() -> RedisLikeManager:
    return RedisLikeManager(redis, key_prefix='fastapi_users_likes:')
