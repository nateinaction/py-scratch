# https://www.hackerrank.com/challenges/cut-the-sticks/problem

import unittest


def cutTheSticks(arr):
    num_cuts = []
    while 0 < len(arr):
        num_cuts.append(len(arr))
        min_el = min(arr)
        arr = [el - min_el for el in arr if min_el < el != min_el]
    return num_cuts


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        input_1 = [5, 4, 4, 2, 2, 8]
        expect_1 = [6, 4, 2, 1]
        self.assertEqual(cutTheSticks(input_1), expect_1)

    def test_2(self):
        input_2 = [23, 74, 26, 23, 92, 92, 44, 13, 34, 23, 69, 4, 19, 94, 94, 38, 14, 9, 51, 98, 72, 46, 17, 25, 21, 87, 99, 50, 59, 53, 82, 24, 93, 16, 88, 52, 14, 38, 27, 7, 18, 81, 13, 75, 80, 11, 29, 39, 37, 78, 55, 17, 78, 12, 77, 84, 63, 29, 68, 32, 17, 55, 31, 30, 3, 17, 99, 6, 45, 81, 75, 31, 50, 93, 66, 98, 94, 59, 68, 30, 98, 57, 83, 75, 68, 85, 98, 76, 91, 23, 53, 42, 72, 77]
        expect_2 = [94, 93, 92, 91, 90, 89, 88, 87, 85, 83, 82, 78, 77, 76, 75, 71, 70, 69, 68, 67, 65, 63, 61, 60, 59, 58, 56, 55, 54, 53, 52, 51, 49, 48, 47, 45, 43, 42, 40, 39, 38, 35, 34, 32, 31, 28, 27, 25, 23, 22, 20, 19, 18, 17, 16, 15, 14, 13, 11, 9, 6, 2]
        self.assertEqual(cutTheSticks(input_2), expect_2)


if __name__ == "__main__":
    unittest.main()
