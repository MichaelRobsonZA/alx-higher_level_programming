#!/usr/bin/python3
"""
This module contains unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_area(self):
        """
        Test the area() method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display(self):
        """
        Test the display() method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        expected_output = "####\n####\n####\n####\n####\n"
        with unittest.mock.patch('sys.stdout', new=unittest.mock.StringIO()) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test the __str__() method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        self.assertEqual(str(rectangle), "Rectangle(4, 5)")

    def test_repr(self):
        """
        Test the __repr__() method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        self.assertEqual(repr(rectangle), "Rectangle(4, 5)")

    def test_update(self):
        """
        Test the update() method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        rectangle.update(6, 7)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        rectangle.update(8, 9, 10, 11, 12)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 9)


if __name__ == '__main__':
    unittest.main()

