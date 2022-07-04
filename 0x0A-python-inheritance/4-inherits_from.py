#!/usr/bin/python3
"""a function that checks if an obj is a child
of a specified class"""


def inherits_from(obj, a_class):
    """function determines if obj is a subclass of a_class
    args:
    obj: the object to be checked
    a_class: the supposed parent class

    Return: True if obj is a subclass otherwise false
    """

    return isinstance(obj, a_class) and type(obj) != a_class
