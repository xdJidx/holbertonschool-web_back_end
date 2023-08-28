#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier

    Args:
        multiplier (float) : Float to multiplier

    Returns:
        float : a function that multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    
    return multiplier_function
