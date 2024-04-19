#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        index_row = []
        for element in row:
            index_row.append(element ** 2)
        new_matrix.append(index_row)
    return new_matrix
