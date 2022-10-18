#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A Class to test MaxInteger function
    """
    def max_integer(self):
        """
        Test Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
        """
        self.assertAlmostEqual(max_integer([6, 8, 2, 5]), 8)
        self.assertAlmostEqual(max_integer([7, 10, 7, 3]), 10)
        self.assertAlmostEqual(max_integer([2, 2, 2, 2.1]), 2.1)
        self.assertEqual(max_integer(["McDonald",45, "Jerry"]), "McDonald")
