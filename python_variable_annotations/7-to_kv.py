#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv

    Args:
        k (str) : simple string, first element of tuple
        v (int or float) : simple int or float, second element of tuple

    Returns:
        tuple : containing the string k and the square of the int/float v
    """
    return k, float(v ** 2)
