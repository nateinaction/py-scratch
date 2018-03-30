#!/bin/python3

import sys


def getMinimumCost(num_flowers, num_customers, flower_base_cost):
    # Verify input valid
    if not flower_base_cost or num_customers == 0:
        return 0

    # Make sure flower_base_cost arr is sorted
    flower_base_cost.sort()

    # Every cycle: each cx buys max cost flower
    min_cost = 0
    for i, flower_cost in enumerate(reversed(flower_base_cost)):
        cycle = i // num_customers
        min_cost += getCost(cycle, flower_cost)

    return min_cost


def getCost(cycle, base_cost):
    return (cycle + 1) * base_cost


if __name__ == '__main__':
    n, k = 3, 3
    c = [2, 5, 6]
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)  # expect 12

    n, k = 3, 2
    c = [2, 5, 6]
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)  # expect 15

    n, k = 3, 2
    c = [6, 5, 2]
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)  # expect 15

    n, k = 5, 1
    c = [1, 2, 3, 4, 5]
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)  # expect 35

    n, k = 75, 21
    c = [164196, 467137, 977470, 817668, 981599, 200118, 292386, 67039, 237227, 320400, 809578, 523670, 891591, 752075, 625021, 588081, 104010, 956783, 625841, 580327, 885115, 212071, 550774, 472712, 897296, 803376, 547683, 191613, 568642, 910957, 611419, 944808, 770889, 587671, 513563, 215077, 44921, 418641, 343588, 986674, 19833, 457049, 951743, 412523, 287579, 213723, 450354, 498989, 720861, 154015, 64829, 929501, 854523, 348771, 77457, 238849, 232047, 968324, 289742, 68683, 473927, 837845, 811959, 178999, 195552, 777298, 745013, 249546, 473348, 814703, 621572, 412921, 559006, 351625, 712190]
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)  # expect 68563180
