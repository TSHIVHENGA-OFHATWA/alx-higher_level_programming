#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for loop in range(0, len(names)):
        if names[loop][:2] != "__":
            print("{:s}".format(names[loop]))
