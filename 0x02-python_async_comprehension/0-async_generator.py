#!/usr/bin/env python3
"""The coroutine will loop 10 times, each time asynchronously wait
   1 second, then yield a random number between 0 and 10. Use the
   random module
"""
from typing import Generator
from random import uniform
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """loops 10 times yielding a random value"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
