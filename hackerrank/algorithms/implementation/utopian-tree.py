#!/bin/python3
# https://www.hackerrank.com/challenges/utopian-tree/problem

import unittest


def utopianTree(n):
    tree_size = 1
    for cycle in range(n):
        tree_size = tree_size * 2 if cycle % 2 == 0 else tree_size + 1

    return tree_size


class TestMe(unittest.TestCase):
    def test_1(self):
        n = 0
        expect = 1
        self.assertEqual(expect, utopianTree(n))

    def test_2(self):
        n = 1
        expect = 2
        self.assertEqual(expect, utopianTree(n))

    def test_3(self):
        n = 4
        expect = 7
        self.assertEqual(expect, utopianTree(n))


if __name__ == '__main__':
    unittest.main()
