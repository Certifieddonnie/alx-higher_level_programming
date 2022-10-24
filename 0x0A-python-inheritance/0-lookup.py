#!/usr/bin/python3
"""
This "0-lookup" module
"""


def lookup(obj):
    """
    The Function that returns the list of availbale attributes
    and methods of an object.
    """
    return dir(obj)
