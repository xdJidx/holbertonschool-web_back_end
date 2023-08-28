#!/usr/bin/env python3
"""
3. Tasks
"""
import asyncio
from typing import Awaitable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random
       Creates and returns an asyncio.Task for wait_random coroutine
    Args:
        max_delay (int): number of delay

    Returns:
        Awaitable[float]: Create awaitable float
    """

    return asyncio.create_task(wait_random(max_delay))
