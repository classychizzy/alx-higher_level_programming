#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    keys = list(b_dictionary.keys())

    for i in keys:
        b_dictionary[i] *= 2

    return b_dictionary
