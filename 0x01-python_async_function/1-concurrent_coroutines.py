#!/usr/bin/env python3
"""
This module contains an async routine called wait_n
that takes in 2 int arguments: n and max_delay
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Async coroutine that spawns wait_random
    n times with the specified max_delay

    paramters:
    n,
    max-delay
    """

    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return results
