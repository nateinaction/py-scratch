#!/bin/python3
# https://www.hackerrank.com/challenges/angry-children/problem

import sys


def angryChildren(num_in_group, arr):
    # sort the array
    arr.sort()

    # iterate over array grabbing groups of num_in_group len
    min_unfairness = sys.maxsize
    for i in range(len(arr) - num_in_group + 1):
        group = arr[i:i + num_in_group]
        group_unfairness = group[-1] - group[0]
        min_unfairness = min(group_unfairness, min_unfairness)

    return min_unfairness


if __name__ == "__main__":
    n = 7
    k = 3
    arr = [10, 100, 300, 200, 1000, 20, 30]
    print(angryChildren(k, arr))  # expect 20

    n = 7
    k = 3
    arr = [100, 200, 300, 350, 400, 401, 402]
    print(angryChildren(k, arr))  # expect 2
