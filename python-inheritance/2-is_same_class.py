#!/usr/bin/python3
"""
Function returns True
if object is exactly an instance of the specified class, else False
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class

        Return: True if exact match, else False
    """
    return type(obj) is a_class
