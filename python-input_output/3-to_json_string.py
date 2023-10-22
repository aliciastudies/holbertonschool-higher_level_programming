#!/usr/bin/python3
"""
Function returns JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON rep of str object
    """
    content = json.dumps(my_obj)
    return content
