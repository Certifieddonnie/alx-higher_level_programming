#!/usr/bin/python3
"""
The "0-read_file" module that reads a text file.
"""


def read_file(filename=""):
    """
    Function that reads a text file(UTF8) and prints it to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
