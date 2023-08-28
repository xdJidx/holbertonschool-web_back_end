#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time
     that measures the total execution
     time for wait_n(n, max_delay)

    Args:
        n (int): number of time remot
        max_delay (int): delay maximal

    Returns:
        float: an approximate elapsed time.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
