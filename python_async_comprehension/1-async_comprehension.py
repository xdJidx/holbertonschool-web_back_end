#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension

    Returns:
        List[float]: List of async_generator
    """
    return [i async for i in async_generator()]
