#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    maximum = my_list[0]
    for number in range(len(my_list)):
        if my_list[number] > maximum:
            maximum = my_list[number]
    return (maximum)
