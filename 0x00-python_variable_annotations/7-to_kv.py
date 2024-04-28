#!/usr/bin/env python3
"""
This module contains a type-annotated function to_kv that takes
a string k and an int OR float v as arguments and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This method returns a tuple of k and v
    parameter: k, v
    """

    return (k, v ** 2)
