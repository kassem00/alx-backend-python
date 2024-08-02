#!/usr/bin/env python3
#!/usr/bin/env python3
""" sum mixed list  """
from typing import List, Union
""" sum mixed list  """


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ 
    type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats and returns their sum as a float
    """
    x: float = 0
    for value in input_list:
        x += value
    return x
