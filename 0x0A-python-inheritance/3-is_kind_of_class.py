#!/usr/bin/python3
"""a function that checks if an object is an instance of
a class that is inherited from a specified class"""


def is_kind_of_class(obj, a_class):
    """ a function that uses isinstance() to check
    if obj is an instance of the class a_class

    args:
    obj: the object to be checked
    a_class: the class that is used to verify if obj is
    it's instance
    Return: True if obj is an instance of a_class
    """

    return isinstance(obj, a_class)
