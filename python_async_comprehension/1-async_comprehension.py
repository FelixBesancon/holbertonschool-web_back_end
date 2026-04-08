#!/usr/bin/env python3
"""
Defines a coroutine that collects 10 random numbers using an async generator.
Use an async comprehensing over an async generator."""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """Returns a list of 10 random numbers between 0 and 10."""
    return [n async for n in async_generator()]
