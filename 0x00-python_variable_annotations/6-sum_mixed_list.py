#!/usr/bin/env python3
""" Complex types """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum as float """
    return float(sum(mxd_lst))
