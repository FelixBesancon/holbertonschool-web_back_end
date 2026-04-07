#!/usr/bin/python3
"""Defines a function that returns the sum of a list of floats."""


from typing import List
"""Importing List from the typing module for type annotations."""


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats."""
    return sum(input for input in input_list)
