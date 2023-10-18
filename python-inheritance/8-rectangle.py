#!/usr/bin/python3
"""
class Rectangle inherting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Creating Rectangles
    """
    def __init__(self, width, height):
        """
        Function initialises new Rectangle instance

        Args:
            width: int
            height: int
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
