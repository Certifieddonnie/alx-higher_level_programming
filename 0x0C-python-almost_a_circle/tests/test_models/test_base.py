#!/usr/bin/python3
"""Unittest for base id
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    A Class to test the base.id function
    """
    def test_None_id(self):
        """
        Test Function to test the id = None
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_value_id(self):
        """
        Test Function to test the id with values.
        """
        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_None_id_after(self):
        """
        Test Function to test no value after assign
        """
        b = Base()
        self.assertEqual(b.id, 2)

    def test_nb_private(self):
        """Test nb_objects as a private instance attribute"""
        b = Base(6)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_many_args(self):
        """Testing many arguments"""
        with self.assertRaises(TypeError):
            b = Base(2, 3)

