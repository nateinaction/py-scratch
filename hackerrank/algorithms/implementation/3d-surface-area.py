#!/bin/python3
# https://www.hackerrank.com/challenges/3d-surface-area/problem

import unittest


def surfaceArea(H, W, A):
    # get surface area of top and bottom
    sa = 2 * H * W

    # get surface area of each side
    for i in range(H):
        side_1 = A[i]
        sa = find_sa(side_1, W, sa)
    for i in range(W):
        side_2 = [col[i] for col in A]
        sa = find_sa(side_2, H, sa)

    return sa


def find_sa(col, dimension, sa):
    sa += col[0] + col[-1]
    for i in range(dimension - 1):
        sa += abs(col[i] - col[i + 1])

    return sa


class TestMe(unittest.TestCase):
    def test_1(self):
        H, W = 3, 3
        A = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
        expect = 60
        self.assertEqual(surfaceArea(H, W, A), expect)

    def test_2(self):
        H, W = 1, 10
        A = [[51, 32, 28, 49, 28, 21, 98, 56, 99, 77]]
        expect = 1482
        self.assertEqual(surfaceArea(H, W, A), expect)

    def test_3(self):
        H, W = 10, 1
        A = [[51], [32], [28], [49], [28], [21], [98], [56], [99], [77]]
        expect = 1482
        self.assertEqual(surfaceArea(H, W, A), expect)


if __name__ == "__main__":
    unittest.main()
