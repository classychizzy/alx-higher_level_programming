#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    A = set_1 - set_2
    B = set_2 - set_1
    od_set = A.union(B)
    return od_set
