#!/usr/bin/python3
"""
Function returns True if object is an instance of,
or if the object is an instance of an inherited class, specified class,
else False
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class

        Return: True if exact match, else False
    """
    return isinstance(obj, a_class)
