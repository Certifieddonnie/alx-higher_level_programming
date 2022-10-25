#!/usr/bin/python3
"""
A "3-to_json_string" module
"""
import json

def to_json_string(my_obj):
    """Function that returns the JSON rep of an object"""
    return (json.dumps(my_obj))
