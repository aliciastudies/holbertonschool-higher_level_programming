#!/usr/bin/python3
"""
Function returns object represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns object represented by a JSON str
    """
    return json.loads(my_str)
