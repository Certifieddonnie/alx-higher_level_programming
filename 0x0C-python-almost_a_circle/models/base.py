#!/usr/bin/python3
"""
The Base Module
"""


class Base:
    """
    A Class that has a private attribute and constructor;
    __nb_objects and the __init__ function
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        Args;
            id
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
