#!/usr/bin/python3
"""
The "8-class_to_json" module
"""


def class_to_json(obj):
    """FUnction that returns the dictionary description with simple
    data structure(list, dictionary, string, integer and boolean) for
    JSON serialization of an object.
    Args:
        obj; object
    """
    return (obj.__dict__)
