#!/usr/bin/env python3

""" Annotated function """
from typing import Callable, Iterator


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiply a float with multiplier """
    def f(n: float) -> float:
        """ Starting point """
        return float(n * multiplier)
    return f
