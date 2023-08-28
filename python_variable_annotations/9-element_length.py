#!/usr/bin/env python3
"""
Annotate the below function s parameters
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length

    Args:
        lst (Iterable[Sequence]): all element in list

    Returns:
        List ([Tuple, int]) : return list of Tuple and int in list
    """
    return [(i, len(i)) for i in lst]
