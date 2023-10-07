#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    is_it = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            is_it.append(True)
        else:
            is_it.append(False)
    return is_it
