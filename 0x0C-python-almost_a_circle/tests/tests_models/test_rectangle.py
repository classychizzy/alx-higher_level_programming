#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Rectangle class.
        """
        self.assertIsInstance(Rectangle(5, 8), Base)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 8).height, 8)
        self.assertEqual(Rectangle(5, 8, 0, 0).x, 0)
        self.assertEqual(Rectangle(5, 8, 0, 0).y, 0)
