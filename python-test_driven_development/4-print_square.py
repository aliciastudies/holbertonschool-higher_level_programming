#!/usr/bin/python3
"""
Function that prints square with #
"""


def print_square(size):
    """
    Arg:
        Size: int

    Return:
        None

    Raises:
        TypeError: size must be an int
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for index in range(size):
            print("#", end="")
        print()
