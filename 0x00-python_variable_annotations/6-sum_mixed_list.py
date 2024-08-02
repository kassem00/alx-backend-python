#!/usr/bin/env python3
""" sum_list  """
from typing import List, Union


def sum_mixed_list(input_list: List[Union[float, int]]) -> float:
    """ sum_list """
    x: float = 0
    for value in input_list:
        x += value
    return x
