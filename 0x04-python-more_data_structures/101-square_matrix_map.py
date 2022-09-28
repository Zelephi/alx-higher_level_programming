#!/usr/bin/python3
# 101-square_matrix_map.py
# A function that computes the square value of all integers of a matrix using map.


def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
