#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise
    Arg:
        matrix: a list of lists (assumed to be square)
    """
    matrix_len = len(matrix)
    if matrix_len % 2 == 1:
        mid = matrix_len // 2 + 1
    else:
        mid = matrix_len / 2
    # transpose the matrix
    for i, row in enumerate(matrix):
        if i > mid:
            break
        for j, el in enumerate(row):
            if j == i:
                break
            else:
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = el
    # reverse the matrix
    for row in matrix:
        row_len = len(row)
        for i in range(row_len):
            if i > (row_len // 2):
                break
            temp = row[i]
            row[i] = row[-1 - i]
            row[-1 - i] = temp
