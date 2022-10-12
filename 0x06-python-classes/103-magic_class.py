#!/usr/bin/python3
"""module for MagiClass."""
import math


class MagicClass:
    """defines a magicclass."""
    def __init__(self, radius=0):
        """Initialization of MagicClass"""
        if type(radius) != int or type(radius) != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of the Circle"""
        return((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Circuference of the Circle"""
        return(2 * math.pi * (self.__radius))
