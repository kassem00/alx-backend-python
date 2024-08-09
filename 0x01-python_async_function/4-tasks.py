#!/usr/bin/env python3
"""Module to create an asyncio Task that schedules multiple coroutines."""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create a list of tasks using task_wait_random
    and return their completion times sorted.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
