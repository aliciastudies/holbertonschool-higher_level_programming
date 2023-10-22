#!/usr/bin/python3
"""
Write a function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Return object
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        new_object = json.loads(content)
        return new_object
