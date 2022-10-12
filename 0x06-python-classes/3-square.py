#!/usr/bin/python3
"""The Module 3-square contains a class Square that defines
a square by a private instance attribute, size
and a public instance method, area."""


class Square:
    """The Class Square has a private attrbute, size
    and a public attribute, area."""
    def __init__(self, size=0):
        """Initialization of the class;
        checkers for value of size."""
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This Function returns the area of the square using the size."""
        return (self.__size ** 2)
