#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    i = 0
    while i < len(roman_string):
        if (i == len(roman_string) - 1 or
                rom_val[roman_string[i]] >= rom_val[roman_string[i + 1]]):
            total += rom_val[roman_string[i]]
            i += 1
        else:
            total += rom_val[roman_string[i + 1]] - rom_val[roman_string[i]]
            i += 2
    return total
