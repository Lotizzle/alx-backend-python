#!/usr/bin/env python3
"""
This module contains an async routine called task_wait_n
that takes in 2 int arguments: n and max_delay
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that calls task_wait_random
    n times with specified max_delay
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
