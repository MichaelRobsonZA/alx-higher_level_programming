#!/usr/bin/python3
"""A unit test module for the rectangle model.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Rectangle class.
        """
        self.assertIsInstance(Rectangle(5, 8), Rectangle)
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 8).height, 8)
        self.assertEqual(Rectangle(5, 8, 0, 0).x, 0)
        self.assertEqual(Rectangle(5, 8, 0, 0).y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle('10', 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(None, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(True, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, '13')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, None)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, True)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, '20')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, None)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, True)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, 20, '25')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, 20, None)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            rectangle = Rectangle(10, 13, 20, True)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            rectangle = Rectangle(0, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            rectangle = Rectangle(-10, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            rectangle = Rectangle(10, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) 
            rectangle = Rectangle(10, -13)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')

    def test_area(self):
        """Tests the area method of the Rectangle class.
        """
        self.assertEqual(Rectangle(5, 8).area(), 40)
        self.assertEqual(Rectangle(10, 10).area(), 100)
        self.assertEqual(Rectangle(0, 8).area(), 0)
        self.assertEqual(Rectangle(5, 0).area(), 0)

    def test_display(self):
        """Tests the display method of the Rectangle class.
        """
        expected_output = '########\n' \
                          '########\n' \
                          '########\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle(8, 3).display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Tests the __str__ method of the Rectangle class.
        """
        self.assertEqual(str(Rectangle(5, 8)), '[Rectangle] (1) 0/0 - 5/8')
        self.assertEqual(str(Rectangle(10, 10, 1, 1)), '[Rectangle] (2) 1/1 - 10/10')

    def test_update(self):
        """Tests the update method of the Rectangle class.
        """
        r = Rectangle(5, 5)
        r.update(10)
        self.assertEqual(str(r), '[Rectangle] (10) 0/0 - 5/5')
        r.update(10, 2)
        self.assertEqual(str(r), '[Rectangle] (10) 0/0 - 2/5')
        r.update(10, 2, 3)
        self.assertEqual(str(r), '[Rectangle] (10) 3/0 - 2/5')
        r.update(10, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (10) 3/4 - 2/5')
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (10) 3/4 - 2/5')

    def test_to_dictionary(self):
        """Tests the to_dictionary method of the Rectangle class.
        """
        r = Rectangle(10, 10, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 10, 'height': 10, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()

