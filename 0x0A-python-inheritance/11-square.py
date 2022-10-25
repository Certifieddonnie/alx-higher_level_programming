#!/usr/bin/python3
"""
The "11-square" module'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle with;
    Args:
        size: private
    methods:
        area
    """
    def __init__(self, size):
        """Initialisation of the class with size parameter"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
