#!/usr/bin/python3
"""
class MyList
"""


class MyList(list):
    """
    sort list in ascending order
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
