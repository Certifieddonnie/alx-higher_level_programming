#!/usr/bin/python3
"""
The Function prints a square with the character #
"""


def print_square(size):
    """
    Prints the square by its size

    Args:
        size: Length of Square
    """
    if (not isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
