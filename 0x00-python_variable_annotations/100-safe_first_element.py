#!/usr/bin/env python3
"""
This module contains a type-annotated function with non-specific parameters
"""


from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    This method returns the first element in a sequence or None.
    parameter: lst
    """

    if lst:
        return lst[0]
    else:
        return None
