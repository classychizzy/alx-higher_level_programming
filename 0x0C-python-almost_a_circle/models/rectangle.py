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
    def width(self, value):
        """sets the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x co-ordinate of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x co-ordinate of a rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y co-ordinates of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y co-ordinates of a rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of this rectangle.
        Returns: area
        int: The area of this rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints a text representation of this rectangle.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def __str__(self):
        """Creates a string representation of this polygon.
        Returns:
            str: A string representation of this polygon.
        """
        parts = (
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
        res = '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(
            parts[0], parts[1], parts[2], parts[3], parts[4]
        )
        return res

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.
        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation of this polygon.
        Returns:
            dict: A dictionary representation of this polygon.
        """
        res = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return res
