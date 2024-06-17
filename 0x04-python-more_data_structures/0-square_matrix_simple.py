#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lists in matrix:
        inner_list = []
        for i in lists:
            inner_list.append(i ** 2)
        new_matrix.append(inner_list)
    return new_matrix
