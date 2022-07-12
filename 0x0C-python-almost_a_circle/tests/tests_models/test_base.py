#!/usr/bin/python3
"""test_base module"""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for the initialization of base class"""
    def test_None(self):
        id_init = Base().id
        """assert to check if value of id is none"""
        self.assertEqual(id_init + 1, Base().id)
        self.assertIsNotNone(Base(None).id)
        self.assertEqual('0x10', Base('0x10').id)
        self.assertListEqual([1, 5], Base([1, 5]).id)
        self.assertNotEqual(None, Base(None).id)
        self.assertEqual(False, Base(False).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual(0, Base(0).id)
        self.assertEqual(-10, Base(-10).id)
        self.assertEqual(10, Base(10).id)
        self.assertFalse('nb_objects' in dir(Base))
        self.assertFalse('__nb_objects' in dir(Base))
