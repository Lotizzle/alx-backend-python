#!/usr/bin/env python3
"""
This module contains a function task_wait_random that takes
an integer max_delay and returns a asyncio.Task.
"""

import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random(max_delay)
    """
    async def inner_task():
        result = await wait_random(max_delay)
        return result

    task = asyncio.create_task(inner_task())
    return task
