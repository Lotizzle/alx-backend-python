#!/usr/bin/env python3
"""
This module contains a coroutine called async_generator that takes no arguments
and yields a number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine yields a random number between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
