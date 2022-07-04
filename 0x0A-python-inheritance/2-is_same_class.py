#!/usr/bin/python3
"""a function that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of a_class
    args:
    obj: object to look at
    a_class: class to verify the instance of

    Return: True if obj is an instance of a_class

    """

    return True if type(obj) is a_class else False
