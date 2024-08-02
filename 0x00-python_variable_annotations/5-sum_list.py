#!/usr/bin/env python3
from typing import List
""" sum_list  """


def sum_list(input_list: List[float]) -> float:
    """ sum_list """
    x: float = 0
    for value in input_list:
        x += value
    return x
