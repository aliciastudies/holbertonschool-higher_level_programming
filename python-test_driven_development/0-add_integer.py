#!/usr/bin/python3
"""
func that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
        a: int or float
        b: int or float with default 98

    Return:
        int: sum of a and b

    Raises:
            TypeError: if either a or b are not ints or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
