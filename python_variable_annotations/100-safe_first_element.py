#!/usr/bin/env python3
"""Defines a type-annotated function safe_first_element."""


from typing import Sequence, Optional, Any


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a list if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
