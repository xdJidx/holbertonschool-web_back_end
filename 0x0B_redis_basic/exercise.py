#!/usr/bin/env python3
""" redis module"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """Décorateur pour compter le nombre d'appels à une méthode"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Fonction interne du décorateur"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Décorateur pour enregistrer l'historique des appels"""
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Fonction interne du décorateur"""
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrapper


def replay(method: Callable):
    """Fonction pour rejouer et afficher l'historique des appels"""
    self_ = method.__self__
    stored_name = method.__qualname__
    inputs = stored_name + ":inputs"
    outputs = stored_name + ":outputs"

    print(f"{stored_name} was called {self_._redis.get(stored_name)} times:")
    for input, output in zip(self_._redis.lrange(inputs, 0, -1),
                             self_._redis.lrange(outputs, 0, -1)):
        print(f"{stored_name}(*{input.decode()}) -> {output.decode()}")


class Cache:
    """Classe de cache Redis
    """

    def __init__(self):
        """Constructeur de la classe de modèle Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        """Stocker des données dans le cache Redis"""
        key = str(uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> UnionOfTypes:
        """Récupérer la clé depuis Redis"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """Récupérer une chaîne de caractères"""
        return string.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """Récupère data depuis Redis à l'aide d'une clé et
        les retourne en int"""
        value = self._redis.get(key)
        if value is not None:
            try:
                # Si la valeur est une chaîne d'octets, la convertit
                # en UTF-8 et ensuite en entier
                decoded_value = value.decode('utf-8')
                return int(decoded_value)
            except (UnicodeDecodeError, ValueError):
                pass
        return None
