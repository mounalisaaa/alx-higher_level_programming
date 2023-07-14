#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for row in matrix:
        for elem in row:
            if elem != row[-1]:
                print("{}".format(elem), end=" ")
            else:
                print("{}".format(elem))
