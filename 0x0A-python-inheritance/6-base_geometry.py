#!/usr/bin/python3
"""class that raises an exception"""


class BaseGeometry:
    """a class BaseGeometry that raises an exception"""

    def __init__(self):
        """instantiation of an instance"""
        pass

    def area(self):
        """a function that raises an exception
        if it's area is not implemented"""

        raise Exception("area() is not implemented")
