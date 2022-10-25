#!/usr/bin/python3
"""
The "5-save_to_json_file" module
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
