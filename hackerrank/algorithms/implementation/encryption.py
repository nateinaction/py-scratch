#!/bin/python3
# https://www.hackerrank.com/challenges/encryption/problem

import sys
import math

def encryption(s):
    s = s.replace(" ", "")
    square = math.sqrt(len(s))
    square_max = int(math.ceil(square))

    cols = []
    for col in range(square_max):
        cols.append(s[col::square_max])

    return " ".join(cols)

if __name__ == "__main__":
    s = "have a nice day"
    result = encryption(s)
    print(result)
