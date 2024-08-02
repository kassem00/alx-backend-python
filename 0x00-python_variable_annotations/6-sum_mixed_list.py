#!/usr/bin/env python3
from typing import List, Union
""" sum mixed list  """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats and
    returns their sum as a float
    """
    x: float = 0
    for value in mxd_lst:
        x += value
    return x
