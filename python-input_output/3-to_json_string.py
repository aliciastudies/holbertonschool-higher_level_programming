#!/usr/bin/python3
import json
"""
Function returns JSON representation of an object(string)
"""


def to_json_string(my_obj):
    """
    Returns JSON rep of str object
    """
    content = json.dumps(my_obj)
    return content
