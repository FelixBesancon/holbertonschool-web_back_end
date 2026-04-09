#!/usr/bin/env python3
"""Defines a type-annotated function zoom_array."""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list containing the same elements as lst,
    but zoomed in by the given factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
