#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import unittest


def breakingRecords(score):
    max, min = score[0], score[0]
    max_time_broken, min_times_broken = 0, 0
    for i in range(1, len(score)):
        if score[i] < min:
            min = score[i]
            min_times_broken += 1
        elif max < score[i]:
            max = score[i]
            max_time_broken += 1

    return [max_time_broken, min_times_broken]


class TestMe(unittest.TestCase):
    def test_1(self):
        arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        expect = [2, 4]
        self.assertEqual(breakingRecords(arr), expect)


if __name__ == '__main__':
    unittest.main()
