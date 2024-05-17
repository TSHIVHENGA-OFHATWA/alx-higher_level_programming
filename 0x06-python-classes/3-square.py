#!/usr/bin/python3


"""
The module defines a class Squares.

The module contains:
    - A sheband line specifying the path to the python interpreter.
    - A square class with a docstring debribing its purpuse.
"""


class Square:
    """
        A class used to represent a Square.

        Args:
            size (int): The size of the square (optional, default is 0).

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find the area of square"""
        return self.__size ** 2

    @property
    def get_size(self):
        """Return the size of the square."""
        return self.__size

    @get_size.setter
    def set_size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
