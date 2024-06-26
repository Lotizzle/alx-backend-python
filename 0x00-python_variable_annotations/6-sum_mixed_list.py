#!/usr/bin/env python3
"""
This module contains a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This method takes a mixed list and returns a float
    parameter: mxd_list
    """

    return sum(mxd_lst)
