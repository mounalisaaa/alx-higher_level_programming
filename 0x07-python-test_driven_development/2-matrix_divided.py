#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_element = round(elem / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix