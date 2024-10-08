#!/usr/bin/env python3
"""Module containing the wait_random coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random coroutine """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
