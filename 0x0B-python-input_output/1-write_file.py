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
    """
    with open("filename", "w+") as f:
        write_file = f.write(text)
    return write_file
