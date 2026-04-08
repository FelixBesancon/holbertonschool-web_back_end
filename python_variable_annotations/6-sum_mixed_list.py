"""Defines a function that returns the sum of a list of integers and floats."""


from typing import List, Union
"""Importing List and Union from the typing module for type annotations."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats."""
    return float(sum(mix for mix in mxd_lst))
