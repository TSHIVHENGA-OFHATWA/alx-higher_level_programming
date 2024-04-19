#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = len(my_list)
    for num in range(count):
        print("{:d}".format(my_list[num]))
