#!/usr/bin/python3
"""
The "2-is_same_class" module
"""


def is_same_class(obj, a_class):
    """
    A Function that returns True if the object is exactly an instance
    of the specified class; otherwise False.
    Args:
        obj: object
        a_class: the class
    """
    if type(obj) == a_class:
        return True
    return False
