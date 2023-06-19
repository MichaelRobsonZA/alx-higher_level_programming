#!/usr/bin/python3
"""
Unittests for the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_area(self):
        """
        Test the area method of Base class.
        """
        base = Base(5, 10)
        self.assertEqual(base.area(), 50)

    def test_perimeter(self):
        """
        Test the perimeter method of Base class.
        """
        base = Base(5, 10)
        self.assertEqual(base.perimeter(), 30)

    def test_str(self):
        """
        Test the __str__ method of Base class.
        """
        base = Base(5, 10)
        self.assertEqual(str(base), "Base(5, 10)")

    def test_repr(self):
        """
        Test the __repr__ method of Base class.
        """
        base = Base(5, 10)
        self.assertEqual(repr(base), "Base(5, 10)")


if __name__ == '__main__':
    unittest.main()

