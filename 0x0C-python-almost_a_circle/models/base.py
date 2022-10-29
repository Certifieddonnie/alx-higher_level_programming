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
        self.id = id

    @property
    def id(self):
        """
        id property
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        setting the id property.
        if the id is none, __nb_objects increments by one
        else the value is assigned
        """
        if value == None:
            self.__nb_objects += 1
            self.__id = self.__nb_objects
        else:
            self.__id = value
