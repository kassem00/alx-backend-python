#!/usr/bin/env python3
"""Module containing the async_generator coroutine."""

import asyncio
import random
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Coroutine that loops 10 times, asynchronously waits 1 second each time,
    and yields a random number between 0 and 10.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
