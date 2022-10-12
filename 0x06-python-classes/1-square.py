#!/usr/bin/python3
"""The Module 1-square contains a class Square that defines a square:
    private instance attribute, size
"""


class Square:
    """A Class that defines a square by size(private attribute)"""
    def __init__(self, size=0):
        """Initialization of the class with the size parameter."""
        self.__size = size
