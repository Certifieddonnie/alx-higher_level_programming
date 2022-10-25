#!/usr/bin/python3
"""
The "8-rectangle" module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Initialisation with;
        Args:
            @width
            @height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
