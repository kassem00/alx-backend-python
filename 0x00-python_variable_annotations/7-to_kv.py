#!/usr/bin/env python3
""" to_kv function """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function to_kv which takes a string k and an int or float v
    as arguments and returns a tuple. The first element of the tuple is the
    string k. The second element is the square of the int/float v and should
    be annotated as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k and
        the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
