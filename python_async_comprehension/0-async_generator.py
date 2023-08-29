#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
from typing import List


async def async_generator() -> float:
    """async_generator

    Yields:
        float: Random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
