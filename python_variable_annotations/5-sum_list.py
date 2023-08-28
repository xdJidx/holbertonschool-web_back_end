#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list

    Args:
        input_list (float) : list of float to sum

    Returns:
        float : returns their sum as a float.
    """
    return sum(input_list)
