#!/usr/bin/python3
""" a class that inherits from list """


class MyList(list):
    """a subclass of the class list"""

    def print_sorted(self):
        """a function that prints a sorted list"""
        print(sorted(self))
