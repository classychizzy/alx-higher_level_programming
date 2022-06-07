#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        column = row
        for i in column:
            print("{:d}".format(i), end=" " if column != row[-1] else "")
        print()
