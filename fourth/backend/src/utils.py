from functools import lru_cache
from redis import Redis


@lru_cache
def get_redis() -> Redis:
    return Redis(host="localhost", port=6379, db=0)
