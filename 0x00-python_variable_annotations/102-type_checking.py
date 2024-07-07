#!/usr/bin/env python3
"""
This module contains zoom array function
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a list where each element in the original tuple is repeated 'factor' times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be zoomed.
        factor (int): The number of times each element in the tuple should be repeated. Defaults to 2.

    Returns:
        List[int]: A list containing the zoomed elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


# Example tuple of integers
array = (12, 72, 91)

# Zooming the array elements 2 times (default factor)
zoom_2x = zoom_array(array)

# Zooming the array elements 3 times
zoom_3x = zoom_array(array, 3)
