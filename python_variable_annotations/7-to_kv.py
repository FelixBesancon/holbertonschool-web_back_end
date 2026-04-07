#!/usr/bin/python3
"""Defines a type-annotated function to_kv."""


from typing import Union, Tuple
"""Importing the Union and Tuple types from the typing module."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing the key and the square of the value."""
    return (k, float(v * v))
