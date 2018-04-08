"""
[2:04 PM] Michael Sluyter: spiral matrix print -- given an MxN matrix, print it as a spiral, clockwise from the outside in. So if this were your matrix:
[2:04 PM] Michael Sluyter:
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
[2:04 PM] Michael Sluyter: the output should be
[2:05 PM] Michael Sluyter:
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""

import unittest


def spiralize(matrix, spiral=[]):
    # top
    for el in matrix[0]:
        spiral.append(el)

    # right
    for el in [row[-1] for row in matrix[1:]]:
        spiral.append(el)

    # bottom
    for el in reversed(matrix[-1][:-1]):
        spiral.append(el)

    # left
    for el in reversed([row[0] for row in matrix[1:-1]]):
        spiral.append(el)

    new_matrix = [row[1:-1] for row in matrix[1:-1]]
    if len(new_matrix):
        spiral = spiralize(new_matrix, spiral)

    return spiral


class TestThis(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expect = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(spiralize(matrix), expect)


if __name__ == '__main__':
    unittest.main()
