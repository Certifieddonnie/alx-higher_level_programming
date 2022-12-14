#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A Class to test MaxInteger function
    """
    def test_max_integer(self):
        """
        Test Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
        """
        self.assertAlmostEqual(max_integer([6, 8, 2, 5]), 8)
        self.assertAlmostEqual(max_integer([7, 10, 7, 3]), 10)
        self.assertAlmostEqual(max_integer([2, 2, 2, 2.1]), 2.1)
        self.assertEqual(max_integer(["McDonald","Glory", "Jerry"]), "McDonald")

    def test_negative(self):
        """
        testing negatives
        """
        self.assertEqual(max_integer([-2, -3, -1, -6]), -1)
        self.assertEqual(max_integer([8]), 8)
    
    def test_empty(self):
        """
        Empty List
        """
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
