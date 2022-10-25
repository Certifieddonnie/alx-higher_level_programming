#!/usr/bin/python3
"""
The "100-my_int" module
"""


class MyInt(int):
    """A class that inverts the operations;
    == and !=
    """
    def __eq__(self, value):
        """Inverts the == to !="""
        return self.real != value
    
    def __ne__(self, value):
        """Inverts the != to =="""
        return self.real == value
