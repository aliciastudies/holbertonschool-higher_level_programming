#!/usr/bin/python3
"""
Function that appends a string to a text file (UTF8)
Returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends str to txt file
    Returns number of chars added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
