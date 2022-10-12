#!/usr/bin/python3
"""The module 2-square contains a class Square
that defines a square by private attribute size."""


class Square:
    """A class that defines a square by private attribute size"""
    def __init__(self, size=0):
        """Initialization of the class.
        Conditional statements checking the value of size coming in."""
        if (int(size) < 0):
            raise ValueError("size must be >= 0")
        if (type(size) == int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
