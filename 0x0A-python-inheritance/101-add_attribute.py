#!/usr/bin/python3
"""
The "101-add_attribute" module
"""


def add_attribute(obj, attr, value):
    """This Function adds a new attribute to an object
    Args:
        obj: object to accept new attribute
        attr: attribute to be added
        value: attribute's value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
