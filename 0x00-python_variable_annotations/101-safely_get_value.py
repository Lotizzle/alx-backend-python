#!/usr/bin/env python3
"""
This module contains a function safely_get_value
that returns the value of a dict.
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    This method returns the value of a dict using a key
    parameters: dct, key, default
    """

    if key in dct:
        return dct[key]
    else:
        return default
