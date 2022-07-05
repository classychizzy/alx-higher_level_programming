#!/usr/bin/python3
""" a program that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function appends a string at the end of a
    text file
    Args
    filename: name of the file
    text= the text in the file
    Return: contents of the file plus
    appended text
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_write = f.write(text)
    return append_write
