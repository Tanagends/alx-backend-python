#!/usr/bin/env python3
"""a measure_runtime coroutine that will execute async_comprehension
   four times in parallel using asyncio.gather.
   measure_runtime should measure the total runtime and return it.
   Notice that the total runtime is roughly 10 seconds, explain it
   to yourself.
"""
import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
       using asyncio.gather
    """

    init: float = perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    final: float = perf_counter()

    return final - init
