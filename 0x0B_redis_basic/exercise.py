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
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(input_key, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(output))
            return output
        return wrapper

    @staticmethod
    def replay(method: Callable):
        cache = Cache()  # Create a new Cache instance
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        input_list = cache._redis.lrange(input_key, 0, -1)
        output_list = cache._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(input_list)} times:")
        for input_args, output_value in zip(input_list, output_list):
            print(f"{method.__qualname__}(*{input_args.decode('utf-8')})
                  -> {output_value.decode('utf-8')}")

    @call_history
    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

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
