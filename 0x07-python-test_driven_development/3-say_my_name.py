#!/usr/bin/python3
"""
The Function prints my name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first and last name

    Args:
        first_name
        last_name
    """
    if (not isinstance(first_name, str)):
        raise TypeError('first_name must be a string')
    if (not isinstance(last_name, str)):
        raise TypeError('last_name must be a string')
    if last_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
