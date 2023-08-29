#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime

    Returns:
        float: Measure time to run async_comprehension 4 times
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
