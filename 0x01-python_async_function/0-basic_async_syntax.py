#!/usr/bin/env python3
"""Module containing the async_generator coroutine."""

import asyncio
import random


async def wait_random(n=1):
    x = random.uniform(0, n)
    await asyncio.sleep(n)
    return x
