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
        ValueError: If a or b are NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a != a or abs(a) == float('inf')):
        raise ValueError("cannot convert float NaN or infinity to integer")
    if isinstance(b, float) and (b != b or abs(b) == float('inf')):
        raise ValueError("cannot convert float NaN or infinity to integer")

    return int(a) + int(b)
