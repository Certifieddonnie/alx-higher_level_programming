#!/usr/bin/python3
"""
The "10-student" module
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

    def to_json(self, attrs=None):
        """Retrives the dict rep of a student instance
        if attrs is a list of stings, rep only those attributes
        included in the list
        """
        if type(attrs) == list and \
                all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
