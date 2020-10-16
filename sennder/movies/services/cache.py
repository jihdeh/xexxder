import json

from django.conf import settings
import redis


class RedisCache:
    def __init__(self, ttl=settings.REDIS_TTL):
        self._redis = redis.StrictRedis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
        )
        self.ttl = ttl

    def set(self, key: str, value: list):
        """ Set adds a key/value pair to the cache."""
        set_value = self._redis.set(key, json.dumps(value))
        self._redis.expire(key, self.ttl)
        return set_value

    def get(self, key: str):
        """ Get retrieves the value of the given key from cache."""
        value = self._redis.get(key)
        valid_types = type(value) == str or type(value) == bytes
        if value and valid_types:
            value = json.loads(value)
            return value
