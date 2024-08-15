#!/usr/bin/python3
"""
Function that adds two integers or floats.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats. Floats are cast to integers.

    Args:
        a (int, float): The first value.
        b (int, float, optional): The second value, default is 98.

    Returns:
        int: The result of adding a and b after casting them to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

