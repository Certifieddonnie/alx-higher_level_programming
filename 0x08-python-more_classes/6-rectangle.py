#!/usr/bin/python3
"""
The "6-rectangle" module
"""


class Rectangle:
    """
    A Rectangle Class with
    width and height properties

    Args:
        number_of_instances: times the class is created.
    """

    number_of_instances = 0

    def __str__(self):
        """
        prints the rectangle my way
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return self.my_print()

    def __init__(self, width=0, height=0):
        """
        Initialization Funtion

        Args:
            width: width of rectangle , default 0.
            height: rectangle's height, default 0.
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """
        return that product of height and width of the
        rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        2(width) + 2(height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2*self.__width) + (2*self.__height))

    def my_print(self):
        """
        prints the rectangle
        """
        pos = ""
        for i in range(self.__height):
            for j in range(self.__width):
                pos += "#"
            if i < self.__height - 1:
                pos += "\n"
        return pos

    def __repr__(self):
        """String Representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when class is deleted"""
       type(self).number_of_instances -= 1
        print("Bye rectangle...")
