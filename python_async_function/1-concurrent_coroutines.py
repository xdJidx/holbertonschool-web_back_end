#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines
at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n

    Args:
        n (int): number of time you will spawn
        max_delay (int):  times to delay
    Returns:
        float: return the list of all the delays
    """
    delays = []

    async def collect_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(collect_delay() for _ in range(n)))

    return sorted(delays)
