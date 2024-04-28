#!/usr/bin/env python3
"""
This module contains a type-annotated function, element_length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This method returns a list of tuples
    parameter: lst
    """

    return [(i, len(i)) for i in lst]
