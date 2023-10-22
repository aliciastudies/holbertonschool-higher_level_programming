#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
Returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes str to txt file
    Returns:
        int: number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
