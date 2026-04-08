#!/usr/bin/env python3
"""Defines a task_wait_n function that takes in 2 integer arguments."""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values) sorted from the shortest.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    wait_list = []

    for task in asyncio.as_completed(tasks):
        wait_list.append(await task)

    return wait_list
