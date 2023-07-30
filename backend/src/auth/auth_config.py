from fastapi_users.authentication import BearerTransport, AuthenticationBackend

import redis.asyncio
from fastapi_users.authentication import RedisStrategy

redis = redis.asyncio.from_url("redis://redis:6379", decode_responses=True)

bearer_transport = BearerTransport(tokenUrl="auth/login")


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600, key_prefix='TEST_token')


auth_backend = AuthenticationBackend(
    name="redis_bearer",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)
