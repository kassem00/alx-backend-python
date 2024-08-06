#!/usr/bin/env python3
"""Module containing the async_comprehension coroutine."""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async_generator,
    and returns them in a list.
    """
    return [i async for i in async_generator()]
