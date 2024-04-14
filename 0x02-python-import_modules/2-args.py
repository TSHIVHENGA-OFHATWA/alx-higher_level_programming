#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    length = len(argv) - 1

    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    for argumnt in range(length):
        print("{}: {:s}".format(argumnt + 1, argv[argumnt + 1]))
