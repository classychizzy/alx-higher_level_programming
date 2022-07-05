#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """read a file with UTF8 encoding """
    with open(filename) as f:
        for line in f:
            print(line, end="")
