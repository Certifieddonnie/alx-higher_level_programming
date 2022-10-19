#!/usr/bin/python3
"""
The "101-locked_class" module
"""


class LockedClass:
    """
    A class that allows no other attribute than
    instance attribute first_name.
    """

    __slots__ = ["first_name"]
