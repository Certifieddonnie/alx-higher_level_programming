#!/usr/bin/python3
#   A function that executes a function safely.
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as d:
        print("Exception: {}".format(d), file=sys.stderr)
        return (None)
