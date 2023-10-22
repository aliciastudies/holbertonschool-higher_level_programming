#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """
    Define class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiate attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for at in attrs:
            if hasattr(self, at):
                new_dict[at] = getattr(self, at)
        return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
