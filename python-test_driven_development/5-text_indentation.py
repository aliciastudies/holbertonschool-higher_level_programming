#!/usr/bin/python3
"""
Function that prints text with 2 new lines
after each these characters: . ? :
"""


def text_indentation(text):
    """
    Arg:
        text: str

    Return:
        None

    Raise:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punc = [".", "?", ":"]
    current = ""
    for char in text:
        current = current + char
        if char in punc:
            print(current)
            print()
            current = ""
    if current:
        print(current, end="")
