#!/bin/python3
# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

import unittest


def get_layers(matrix, layers_arr=None):
    if not layers_arr:
        layers_arr = []

    new_layer = []
    # top
    for el in matrix[0]:
        new_layer.append(el)

    # right
    for el in [row[-1] for row in matrix[1:]]:
        new_layer.append(el)

    # bottom
    for el in reversed(matrix[-1][:-1]):
        new_layer.append(el)

    # left
    for el in reversed([row[0] for row in matrix[1:-1]]):
        new_layer.append(el)

    layers_arr.append(new_layer)

    new_matrix = [row[1:-1] for row in matrix[1:-1]]
    if len(new_matrix) and len(new_matrix[0]):
        layers_arr = get_layers(new_matrix, layers_arr)

    return layers_arr


def set_matrix(layers_arr, num_rows, num_columns):
    # top
    matrix = [layers_arr[0][:num_columns]]

    # inner layers
    if num_rows == 3:
        matrix.append([layers_arr[0][-1], layers_arr[0][num_columns]])
    elif 3 < num_rows:
        inner_rows = set_matrix(layers_arr[1:], num_rows - 2, num_columns - 2)
        for inner_column_i, inner_columns in enumerate(inner_rows):
            matrix.append([layers_arr[0][-(inner_column_i + 1)]] + inner_columns + [layers_arr[0][num_columns + inner_column_i]])

    # bottom 0, 2  4, 7
    matrix.append(list(reversed(layers_arr[0]))[num_rows - 2:num_rows + num_columns - 2])

    return matrix


def matrixRotation(matrix, num_rotations, num_rows, num_columns):
    layers_arr = get_layers(matrix)
    new_layers_arr = []
    for layer in layers_arr:
        real_rotations = num_rotations % len(layer)
        new_layers_arr.append(layer[real_rotations:] + layer[:real_rotations])

    return set_matrix(new_layers_arr, num_rows, num_columns)


class TestMe(unittest.TestCase):
    # @unittest.skip("skipping for now")
    def test_1(self):
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
        num_rotations, num_rows, num_columns = 1, 4, 5
        expect = [[2, 3, 4, 5, 10], [1, 8, 9, 14, 15], [6, 7, 12, 13, 20], [11, 16, 17, 18, 19]]
        self.assertEqual(expect, matrixRotation(matrix, num_rotations, num_rows, num_columns))

    # @unittest.skip("skipping for now")
    def test_2(self):
        matrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22], [25, 26, 27, 28]]
        num_rotations, num_rows, num_columns = 7, 5, 4
        expect = [[28, 27, 26, 25], [22, 9, 15, 19], [16, 8, 21, 13], [10, 14, 20, 7], [4, 3, 2, 1]]
        self.assertEqual(expect, matrixRotation(matrix, num_rotations, num_rows, num_columns))


if __name__ == '__main__':
    unittest.main()
