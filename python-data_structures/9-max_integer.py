#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_value = my_list[0]
    if my_list is not None:
        for i in range(1, length):
            if my_list[i] > max_value:
                max_value = my_list[i]
    return max_value
