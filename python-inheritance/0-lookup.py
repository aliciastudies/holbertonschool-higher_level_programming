#!/usr/bin/python3
"""
Function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Arg:
        obj: object

    Return:
        list
    """
    return (dir(obj))
