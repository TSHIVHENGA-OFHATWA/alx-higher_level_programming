#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    for num in range(count):
        print("{:d}".format(my_list[num]))
