#!/usr/bin/python3
"""a function that creates an object from a json file"""


def load_from_json_file(filename):
    """a function that converts a json file back to an
    object
    Args
    filename: the name of the json file
    Return: object format of the file
    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
