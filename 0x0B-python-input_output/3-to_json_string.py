#!/usr/bin/python3
"""a program that returns the JSON
representation of an object"""


def to_json_string(my_obj):
    """a function that returns the json representation
    of an object

    Args
    my_obj: the object that is converted to JSON
    Return: JSON representation of my_obj
    """
    import json
    return json.dumps(my_obj)
