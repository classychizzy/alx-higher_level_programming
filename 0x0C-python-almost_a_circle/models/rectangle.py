#!/usr/bin/python3
"""rectangle.py module"""


from .base import Base


class Rectangle(Base):
    """Represents a rectangle
    Args:
    width: defines the width of the rectangle
    height: defines the height of the rectangle
    x: the horizontal position of the
    y:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle class"""

        super().__init__(id)
        """calls the parent Base
        and adds new args to the new
        object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of a rectangle"""
        self.__width = width

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of a rectangle"""
        self.__height = height

    @property
    def x(self):
        """gets the x co-ordinate of a rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the x co-ordinate of a rectangle"""
        self.__x = x

    @property
    def y(self):
        """gets the y co-ordinates of a rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the y co-ordinates of a rectangle"""
        self.__y = y
