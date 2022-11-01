#!/usr/bin/python3
"""
The Base Module
"""
import json
from io import StringIO


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries
        Args:
            list_dictionaries is a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            io = StringIO()
            json.dump(list_dictionaries, io)
            return (io.getvalue())

    @classmethod
    def save_to_file(cls, list_objs):
        """It writes the JSON string rep of list_objs to a file
        Args:
            list_objs is a list of instances who inherits of Base
        """
        lst = []
        if list_objs is not None:
            for i in list_objs:
                lst.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string is a string representation of a list of dict
        """
        lst = []
        if json_string is None or len(json_string) == 0:
            return lst
        else:
            io = StringIO(json_string)
            return (json.load(io))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        lst = []
        if (filename):
            with open(filename, "r") as f:
                lst = cls.from_json_string(f.read())
            for k, v in enumerate(lst):
                lst[k] = cls.create(**lst[k])
        else:
            return lst
        return lst
