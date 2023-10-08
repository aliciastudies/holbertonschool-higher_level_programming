#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_score = 0
    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
    for key, value in a_dictionary.items():
        if value == highest_score:
            return key
