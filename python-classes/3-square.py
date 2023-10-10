#!/usr/bin/python3
"""
Defining a Square
"""


class Square:
    """
    Adding a private attribute
    """
    def __init__(self, size=0):
        """
        adding TypeError and ValueError
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
