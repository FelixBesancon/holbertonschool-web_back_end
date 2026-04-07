#!/usr/bin/python3
"""Defines a type-annotated function make_multiplier."""


from typing import Callable
"""Importing the Callable type from the typing module for type annotations."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier."""

    def multiply(value: float) -> float:
        """Returns the product of the value and the multiplier."""
        return float(value * multiplier)

    return multiply
