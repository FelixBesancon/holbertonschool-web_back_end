#!/usr/bin/env python3
"""Defines an asynchronous coroutine that takes in 2 integer arguments."""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values) sorted from the shortest
    """
    coros = [wait_random(max_delay) for _ in range(n)]

    wait_list = []

    for coro in asyncio.as_completed(coros):
        wait_list.append(await coro)

    return wait_list
