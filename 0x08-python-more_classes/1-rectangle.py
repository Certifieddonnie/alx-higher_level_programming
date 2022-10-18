#!/usr/bin/python3
"""
The "1-rectangle" module
"""


class Rectangle:
    """
    A Rectangle Class with
    width and height properties
    """
    def __init__(self, width=0, height=0):
        """
        Initialization Funtion

        Args:
            width: width of rectangle , default 0.
            height: rectangle's height, default 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property of the breadth of rectangle
        Raises:
            TypeError: width muat be an integer
            ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle

        Args:
            value: width of rectangle
        """
        if (not isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        property of the height/length of rectnagle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the length of the rectangle

        Args:
            value: height of rectangle
        """
        if (not isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
