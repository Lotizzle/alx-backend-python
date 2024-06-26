#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine
that takes in an integer argument
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine that waits for a
    random delay between 0 and max_delay

    parameter:
    max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
