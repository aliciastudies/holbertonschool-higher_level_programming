#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    biggest = my_list[0]
    for challenger in my_list:
        if challenger > biggest:
            biggest = challenger
    return biggest
