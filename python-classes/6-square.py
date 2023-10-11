#!/usr/bin/python3
"""
Defining class Square:
private attribute size, getter and setter, public method
"""


class Square:
    """
    Creating Squares

    Attributes:
        __size (int): Size of square
        __position (int): Position of square

    Methods:
        __init__(self, size=0, position=(0, 0)): initiliases square with default 0 and position 0, 0
        area(self): calculates current square area
        my_print(self): prints square with the character #

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises new Square instance

        Args:
            size (int): size of the square
            position (int): position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Function to get value of __size

        Returns:
            __size
        """
        return self.__size

    @property
    def position(self):
        """
        Function to get value of __position

        Returns:
            __position
        """
        return self.__position

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
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple ")
        self.__position = value

    def area(self):
        """
        Function that calculates the current square area

        Return:
            Current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Function prints square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()