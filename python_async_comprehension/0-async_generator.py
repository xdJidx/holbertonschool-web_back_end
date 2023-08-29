#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio, random


async def async_generator():

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
