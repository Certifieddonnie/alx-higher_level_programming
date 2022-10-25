#!/usr/bin/python3
"""
The "4-from_json_string" module
"""
import json


def from_json_string(my_str):
    """Function that returns an object(Python data struct)
    represented by a JSON string.
    """
    return (json.loads(my_str))
