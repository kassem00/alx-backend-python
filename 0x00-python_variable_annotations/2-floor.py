#!/usr/bin/env python3

import math
from typing import Dict
""" floor div """


def floor(n: float) -> int:
    """ floor div """
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1 if n != int(n) else int(n)
