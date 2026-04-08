#!/usr/bin/env python3
"""Defines a function that returns the floor of a float."""


def floor(n: float) -> int:
    """Returns the floor of a float."""
    return int(n - 1) if (n < 0 and int(n) != n) else int(n)
