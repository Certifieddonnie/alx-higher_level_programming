#!/usr/bin/python3
"""
The "1-write_file" module that writes a string to a text file(UTF8)
"""


def write_file(filename="", text=""):
    """Function that writes a string to the text file"""
    with open(filename,"w",encoding="utf-8") as f:
        return (f.write(text))
