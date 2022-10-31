#!/usr/bin/python3
"""Unittest for rectangle class
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A Test for the Rectangle Class
    """
    @classmethod
    def setUpClass(cls):
        """Setup"""
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10, 4, 5)
        cls.r3 = Rectangle(2, 10, 4, 5, 20)
        cls.r4 = Rectangle(10, 2)

    def test_id(self):
        """
        Test for ID
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 20)
        self.assertEqual(self.r4.id, 3)

    def test_x(self):
        """
        Test for x and y
        """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 4)
        self.assertEqual(self.r4.x, 0)
        

    def test_y(self):
        """Test for y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r3.y, 5)
        self.assertEqual(self.r4.y, 0)

    def test_width(self):
        """Test width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 2)
        self.assertEqual(self.r4.width, 10)

    def test_height(self):
        """Test height"""
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 10)
        self.assertEqual(self.r4.height, 2)

    def test_for_more_args(self):
        """Testing many arguments"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 2, 0, 0, 20, 50)

    def test_for_few_args(self):
        """Testing few arguments"""
        with self.assertRaises(TypeError):
            r6 = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(10)

    def test_width_private(self):
        """Test width as a private instance attribute"""
        r7 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(self.r7.width)
        with self.assertRaises(AttributeError):
            print(self.r7.__width)

    def test_height_private(self):
        """Test height as a private instance attribute"""
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(self.r.height)
        with self.assertRaises(AttributeError):
            print(self.r.__height)

    def test_x_private(self):
        """Test x as a private instance attribute"""
        r = Rectangle(10, 2, 5, 5)
        with self.assertRaises(AttributeError):
            print(self.r.x)
        with self.assertRaises(AttributeError):
            print(self.r.__x)

    def test_y_private(self):
        """Test y as a private instance attribute"""
        r = Rectangle(10, 2, 5, 5)
        with self.assertRaises(AttributeError):
            print(self.r.y)
        with self.assertRaises(AttributeError):
            print(self.r.__y)

    def test_width_typeerror(self):
        """Test for non int width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hey", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 2)

    def test_height_typeerror(self):
        """Test for non int height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, False)

    def test_x_typeerror(self):
        """Test for non int x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, "Hi")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2, True)

    def test_y_typeerror(self):
        """Test for non int y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 1, "Hi")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2, 1, False)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Test Area"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)
        self.assertEqual(self.r4.area(), 20)

    def test_area_args(self):
        """Test many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r1.area(1)

    def test_display(self):
        """Testing the display method"""
        r = Rectangle(4, 3, 2, 2, 4)
        with StringIO() as f, redirect_stdout(f):
            r.display()
            output = f.getvalue()
            self.assertEqual(output, ("#" * 4 + "\n") * 3)

    def test_display_many_args(self):
        """Testing display with many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

