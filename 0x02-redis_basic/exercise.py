#!/usr/bin/env python3
"""Creates a class, generates a key with uuid
   stores data inside the key.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Class that stores data in a redis key"""
    def __init__(self) -> None:
        """Creates a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """method that Creates a key and store data"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes,
                                                    int, float]:
        """
        get method that take a key string argument and an
        optional Callable argument named fn. This callable
        will be used to convert the data back to the desired format.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(key)
        return value

    def get_str(self, key: str) -> str:
        """
          This will be used to convert the data back to the string.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return data.decode('utf-8')

    def get_int(self, key):
        """
          This will be used to convert the data back to int.
        """

        data = self._redis.get(key)
        if data is None:
            return None
        return int(data.decode("utf-8"))
