#!/usr/bin/env python3
"""
This module contains a coroutine called async_comprehension
that takes no arguments.
"""

from typing import List
from asyncio import gather
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """

    async_gen = async_generator()
    result = [num async for num in async_gen]
    return result
