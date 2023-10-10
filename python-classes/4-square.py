#!/usr/bin#!/usr/bin/python3
"""
Defining a Square
"""


class Square:
    """
    Creating Squares

    """
    def __init__(self, size=0):
        """
        Initialises new Square instance
        
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Function to get value of __size

        Returns:
            __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function to set value of __size

        Args:
            value (int): size of square

        Raises:
            TypeError: value must be an int
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Function that calculates the current square area

        Return:
            Current square area
        """
        return self.__size ** 2
