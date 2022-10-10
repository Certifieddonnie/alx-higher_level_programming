#!/usr/bin/python3
# A Function that prints an integer with "{:d}".format().

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="")
        print()
        return(True)
    except (ValueError, TypeError):
        return(False)
