#!/usr/bin/env python3
""" Async generator """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async generator """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
