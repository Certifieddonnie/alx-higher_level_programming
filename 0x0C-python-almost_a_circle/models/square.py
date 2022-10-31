#!/usr/bin/python3
"""
A Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square Class that inherits from Rectangle"""

    def __str__(self):
        """String Representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
                .format(self.id, self.x, self.y, self.width)

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the Square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attribute"""
        if len(args):
            for idx, attr in enumerate(args):
                if idx == 0:
                    self.id = attr
                elif idx == 1:
                    self.size = attr
                elif idx == 2:
                    self.x= attr
                elif idx == 3:
                    self.y = attr
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dict rep of a square"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
