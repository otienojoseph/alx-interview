#!/usr/bin/env python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix clockwise

    Args:
        matrix (list of list of int): The (n x n) matrix

    Returns:
        None: The matrix is modified in place
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
