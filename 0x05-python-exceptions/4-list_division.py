#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                val1 = my_list_1[i]
                val2 = my_list_2[i]
            except IndexError:
                print("out of range")
                break
            try:
                if isinstance(val1, (int, float))\
                and isinstance(val2, (int, float)):
                    if val2 != 0:
                        result.append(val1 / val2)
                    else:
                        result.append(0)
                        print("division by 0")
                else:
                    result.append(0)
                    print("wrong type")
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
    finally:
        return result
