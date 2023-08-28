#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list

    Args:
        mxd_lst (int, float) : list of int and float to sum

    Returns:
        float : returns their sum as a float.
    """
    return sum(mxd_lst)
