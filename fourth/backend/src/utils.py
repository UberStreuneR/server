from functools import lru_cache
from redis import Redis


@lru_cache
def get_redis() -> Redis:
    return Redis(host="redis", port=6379, db=0)
