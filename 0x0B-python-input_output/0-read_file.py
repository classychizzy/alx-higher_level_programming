#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """read a file with UTF8 encoding """
    with open("./tests/my_file_0.txt", encoding="utf-8") as filename:
        for line in filename:
            print(line, end="")
