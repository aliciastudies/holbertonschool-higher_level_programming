#!/usr/bin/python3
"""
class Square inherting from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creating Squares
    """
    def __init__(self, size):
        """
        Function initialises new Square instance

        Arg:
            size: int
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)
