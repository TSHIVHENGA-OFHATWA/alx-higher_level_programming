#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for loop in range(1, len(argv)):
        result += int(argv[loop])
        print("{}".format(result))
