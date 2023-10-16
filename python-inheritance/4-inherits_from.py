#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class,
else False.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class

        Return: True if exact match, else False
    """
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    return False
