#!/usr/bin/python3
"""a program that converts an object to a text file"""


def save_to_json_file(my_obj, filename):
    """a function that saves an object as a json file
    Args
    my_obj: the object to be converted
    filename: the name of the text file containing the
    json format of the object
    Return: the object as a textfile
    """
    import json
    with open (filename, "w", encoding="utf-8") as f:
       return json.dump(my_obj, f)
