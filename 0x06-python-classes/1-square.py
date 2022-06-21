#!/usr/bin/python3
"""creating a class with private attribute"""


class Square:
    """Representation of a square.
    with a private attribute size"""
    def __init__(self, size):
        """private attribute size"""
        self.__size = size
