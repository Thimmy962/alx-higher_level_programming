#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for each in matrix:
        for i in each:
            if i == each[-1]:
                print("{:d}".format(i), end='')
                continue
            print("{:d} ".format(i), end='')
        print()
