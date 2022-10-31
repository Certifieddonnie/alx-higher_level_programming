#!/usr/bin/python3
"""
The Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class that inherits from Base
    """

    def __str__(self):
        """String Representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
                .format(self.id, self.__x, self.__y, self.__width, self.__height)
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the rectangle class
        Args:
            width
            height
            x
            y
            id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the rectangle in stdout with character #"""
        i = 0
        print('\n' * self.__y, end="")
        while (i < self.__height):
            j = 0
            print(" " * self.__x, end="")
            while (j < self.__width):
                print("#", end="")
                j += 1
            print()
            i += 1

    def update(self, *args, **kwargs):
        """Assigns an arguments to each attribute"""
        if (len(args)):
            for idx, attr in enumerate(args):
                if idx == 0:
                    self.id = attr
                elif idx == 1:
                    self.width = attr
                elif idx == 2:
                    self.height = attr
                elif idx == 3:
                    self.x = attr
                elif idx == 4:
                    self.y = attr
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
