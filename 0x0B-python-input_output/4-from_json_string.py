#!/usr/bin/python3
""" a program that converts a json string to an object"""


def from_json_string(my_str):
    """a function that converts a json string to
    an object
    Args:
    my_str: json string to be converted
    Return: object form of the json string
    """
    import json
    return json.loads(my_str)
