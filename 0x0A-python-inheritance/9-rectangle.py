#!/usr/bin/python3
"""
The "9-rectangle" module
"""


class BaseGeometry:
    """
    A class with two public instance methods;
    @area: raises an Exception
    @integer_validator: raises Type and Value Error.
    """
    def __init__(self):
        """Initialisation"""

    def area(self):
        """Area that raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks the parameter and raises
        TypeError and ValueError if conditions aren't met
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """
        String Representation of a rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
