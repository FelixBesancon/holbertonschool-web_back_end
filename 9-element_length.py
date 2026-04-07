#!/usr/bin/python3
"""Defines a type-annotated function element_length."""


from typing import List, Tuple, Iterable, Sequence
"""
Importing List, Tuple, Iterable, and Sequence from the typing module
for type annotations.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the
    input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
