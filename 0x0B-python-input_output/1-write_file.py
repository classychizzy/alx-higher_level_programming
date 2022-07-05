#!/usr/bin/python3
""" module 1
a function that writes
lines in a file
"""


def write_file(filename="", text=""):
    """a function that writes content to
    a file or overwrites a file's content
    Args:
    filename: name of the file
    text: content that is placed in the file
    Return: the number of characters
    """
    with open("filename", "w", encoding="utf-8") as f:
        return f.write(text)
