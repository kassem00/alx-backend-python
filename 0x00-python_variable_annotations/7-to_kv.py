#!/usr/bin/env python3
""" sum mixed list  """
from typing import List, Union


def to_kv(k: str, v: List[Union[int, float]]) -> tuple[str, float]:
    """
    type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats and
    returns their sum as a float
    """
    return (k, v ** 2)
