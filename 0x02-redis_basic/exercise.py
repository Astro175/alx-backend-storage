#!/usr/bin/env python3
"""Creates a class, generates a key with uuid
   stores data inside the key.
"""
import redis
import uuid

class Cache:
    """Class that stores data in a redis key"""
    def __init__(self) -> None:
        """Creates a redis instance"""
        self._redis = redis.Redis()
        (self._redis).flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """method that Creates a key and store data"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key


