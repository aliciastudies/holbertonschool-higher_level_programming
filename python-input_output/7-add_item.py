#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file
"""


import os
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""
Add object to JSON file, then load from that file
"""
add_item = "add_item.json"
if not os.path.exists(add_item):
    my_list = []
else:
    my_list = load_from_json_file(add_item)

new_item = sys.argv[1:]
for index in new_item:
    my_list.append(index)
save_to_json_file(my_list, add_item)
