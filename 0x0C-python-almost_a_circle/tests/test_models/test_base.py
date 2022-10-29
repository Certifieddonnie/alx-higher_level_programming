#!/usr/bin/python3
"""Unittest for base id
"""
import unittest
from models.base import Base

class Base(unittest.TestCase):
    """
    A Class to test the base.id function
    """
    def test_None_id(self):
        """
        Test Function to test the id = None
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id(), 1)
        self.assertEqual(b2.id(), 2)
        self.assertEqual(b3.id(), 3)
        self.assertEqual(b4.id(), 4)

    def test_value_id(self):
        """
        Test Function to test the id with values.
        """
        b5 = Base(12)
        b6 = Base(14)
        b7 = Base(15)
        self.assertEqual(b5.id(), 12)
        self.assertEqual(b6.id(), 14)
        self.assertEqual(b7.id(), 25)
