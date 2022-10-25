#!/usr/bin/python3
"""
The "2-append_write" module appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file(UTF8)"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
