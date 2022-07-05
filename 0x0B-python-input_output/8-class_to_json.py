#!/usr/bin/python3
"""a program that converts a class to json"""


def class_to_json(obj):
    """a function that returns the dictionary
    description of an object
    Args
    obj: the object to converted to json
    Return: return the json format of the object
    """
    return obj.__dict__
