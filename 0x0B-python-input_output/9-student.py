#!/usr/bin/python3
"""
The "9-student" module
"""


class Student:
    """A Class that defines a student by:
    public instances;
        first_name
        last_name
        age
    public method;
        to_json
    """
    def __init__(self, first_name="", last_name="", age=None):
        """Initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives the dict rep of a student instance"""
        return self.__dict__
