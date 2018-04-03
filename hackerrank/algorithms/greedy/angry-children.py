#!/bin/python3
# https://www.hackerrank.com/challenges/angry-children/problem

import sys


def angryChildren(num_in_group, arr):
    # sort the array
    arr.sort()

    # calculate all amounts of unfairness and output to an array then grab min of that array
    return min([arr[i + num_in_group - 1] - arr[i] for i in range(n - num_in_group + 1)])


if __name__ == "__main__":
    n = 7
    k = 3
    arr = [10, 100, 300, 200, 1000, 20, 30]
    print(angryChildren(k, arr))  # expect 20

    n = 7
    k = 3
    arr = [100, 200, 300, 350, 400, 401, 402]
    print(angryChildren(k, arr))  # expect 2
