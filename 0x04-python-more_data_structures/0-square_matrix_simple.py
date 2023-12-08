#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        mat = []
        for j in matrix[i]:
            mat.append(j ** 2)
        new_matrix.append(mat)
    return new_matrix
