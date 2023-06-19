#!/usr/bin/python3
"""
Unittests for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_update(self):
        """
        Test the update method of Square class.
        """
        square = Square(5, 1, 2)
        square.update(size=7, x=8, y=9)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)


if __name__ == '__main__':
    unittest.main()

