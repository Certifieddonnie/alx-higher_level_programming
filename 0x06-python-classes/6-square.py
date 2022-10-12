#!/usr/bin/python3
"""The Module 6-square contains the class Square.
it performs area of the square and prints the square
with positioning."""


class Square:
    """The Class that defines a square by:
    private instance attribute: size
    public instance method: area
    public instance method: my_print"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the Class."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in position if type(i) == int and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        """Property of size. it gets the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Property for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property of position function. it gets the data."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter property"""
        if type(position) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if type(i) == int and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """The Function that returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """A Function that prints the square in position."""
        if self.__size == 0:
            print()
        for w in range(self.__position[1]):
            print()
        for i in range(0, self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
