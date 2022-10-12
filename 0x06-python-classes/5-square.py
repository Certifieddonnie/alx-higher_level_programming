#!/usr/bin/python3
"""The Module 5-square contains the class Square.
it performs area of the square and prints the square."""


class Square:
    """The Class that defines a square by:
    private instance attribute: size
    public instance method: area
    public instance method: my_print"""
    def __init__(self, size=0):
        """Initialization of the Class."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getters Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setters Property"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The Function that returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """A Function that prints the square."""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
