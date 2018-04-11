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


def set_layers(matrix, layers_arr, num_rows=0, num_columns=0, level=1):
    current_layer = layers_arr[0]
    # top
    for i in range(num_columns):
        matrix[level - 1][i + level - 1] = current_layer.pop(0)

    # right
    for i in range(1, num_rows):
        matrix[i + level - 1][-level] = current_layer.pop(0)

    # bottom
    for i in range(num_columns - 1):
        matrix[-level][-i - level - 1] = current_layer.pop(0)

    # left
    for i in reversed(range(1, num_rows - 1)):
        matrix[i + level - 1][level - 1] = current_layer.pop(0)

    if len(layers_arr) > 1:
        matrix = set_layers(matrix, layers_arr[1:], num_rows - 2, num_columns - 2, level + 1)

    return matrix


def matrixRotation(matrix, num_rotations, num_rows, num_columns):
    layers_arr = get_layers(matrix)
    new_layers_arr = []
    for layer in layers_arr:
        real_rotations = num_rotations % len(layer)
        new_layers_arr.append(layer[real_rotations:] + layer[:real_rotations])

    return set_layers(matrix, new_layers_arr, num_rows, num_columns)


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

    # @unittest.skip("skipping for now")
    def test_3(self):
        matrix = [[9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927], [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371], [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748], [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864], [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840], [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798], [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547], [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362], [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021], [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]]
        num_rotations, num_rows, num_columns = 40, 10, 8
        expect = [[93754371, 53195748, 90198864, 91644840, 32720798, 35319547, 89653362, 50410021], [31785927, 25289229, 10844931, 97945481, 5270000, 69622764, 27762534, 43779176], [73470430, 90786953, 42430633, 96642353, 88915819, 85669747, 26629304, 86544343], [38021292, 22590518, 90502426, 67042516, 54688734, 32589026, 75398396, 61983443], [21884498, 54702481, 17112485, 5932542, 29446517, 2218936, 71783860, 7071172], [85388216, 71197978, 15654690, 58592832, 49558405, 6331115, 10329789, 56239301], [5103628, 47265349, 54630910, 56425665, 23544383, 86523163, 96382322, 27353496], [60013003, 63729346, 51189, 1408833, 34699742, 38446081, 71055337, 31297360], [9718805, 38615864, 92837327, 6967117, 17741775, 96087879, 30247265, 9392211], [69999937, 79943507, 79354991, 84146680, 58623600, 49469904, 20888810, 55349226]]
        self.assertEqual(expect, matrixRotation(matrix, num_rotations, num_rows, num_columns))


if __name__ == '__main__':
    unittest.main()
