#!/usr/bin/python3
""" Module 1-rectangle
a class that defines a rectangle"""


class Rectangle:
    """a rectangle class defined by it's width and height"""
    def __init__(self, width=0, height=0):
        """initializes an instance of Rectangle

        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle
        Args: value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the height
        Args: height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
