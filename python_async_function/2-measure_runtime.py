#!/usr/bin/env python3
"""
Defines a measure_time function that measures
the total execution time for wait_n(n, max_delay)
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the total execution time for wait_n(n, max_delay)
    divided by n
    """
    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end = time.perf_counter()
    total_time = end - start

    return total_time / n
