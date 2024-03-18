#!/usr/bin/env python3
""" Module for testing client.py """

import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @staticmethod
    def call_history(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(f"{method.__qualname__}:outputs", str(result))
            return result
        return wrapper

    @call_history
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
