#!/usr/bin/env  python3
"""n async routine called wait_n that takes in 2 int arguments
   (in this order): n and max_delay
"""
import asyncio
from typing import List
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay
       return the list of all the delays (float values).
    """
    waits = [task_wait_random(max_delay) for _ in range(n)]
    ordered_times: List[float] = []
    for task in asyncio.as_completed(waits):
        time: float = await task
        ordered_times.append(time)
    return ordered_times
