#!/usr/bin/env python3
"""
This module contains zoom array function
"""


from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    This method zooms in on an array
    parameters: lst, factor
    """

    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
