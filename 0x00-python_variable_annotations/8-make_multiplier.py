#!/usr/bin/env python3
"""
This module contains a type-annotated function make_multiplier
that takes a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns the multiplication of two floats
    parameter: multiplier
    """

    def multiplier_function(x: float) -> float:
        """
        This function multiplies some floats
        parameter: x
        """

        return x * multiplier
    return multiplier_function
