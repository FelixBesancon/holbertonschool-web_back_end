#!/usr/bin/python3
"""
Defines a helper function that returns a tuple of size two containing
a start index and an end index corresponding to the range of indexes
to return in a list for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index
    and an end index.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    if page < 1 or page_size <= 0:
        return (0, 0)
    return (
        (page - 1) * page_size,
        page * page_size
    )
