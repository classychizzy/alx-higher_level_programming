#!/usr/bin/python3
"""base.py module"""


class Base:
    """parent class of all classes in models"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instances of the base class
        Args:
        id = an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
