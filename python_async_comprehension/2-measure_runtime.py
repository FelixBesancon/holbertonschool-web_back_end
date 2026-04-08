#!/usr/bin/env python3
"""
Defines a measure_runtime coroutine that executes async_comprehension
four times in parallel using asyncio.gather and returns the total runtime.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the total runtime of executing async_comprehension
    four times in parallel.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return end - start
