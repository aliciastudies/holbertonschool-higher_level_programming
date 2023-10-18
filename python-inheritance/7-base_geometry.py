#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function validates value

        Args:
            name: str
            value: int

        Return: None

        Raises:
            TypeError:
            ValueError:
        """
        if not isinstance(value, int):
            raise TypeError("{0} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{0} must be greater than 0".format(name))
