#!/usr/bin/python3
"""
class Base
"""


class Base:
    """
    Creating Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises new Base instance

        Arg:
            id: int (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
