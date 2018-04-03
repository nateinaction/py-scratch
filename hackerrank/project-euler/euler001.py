#!/bin/python3


def try_2(n):
    multiples_of_3 = [x for x in range(3, n, 3)]
    multiples_of_5 = [x for x in range(5, n, 5)]

    my_sum = sum(set(multiples_of_3 + multiples_of_5))

    print(my_sum)


def find_max_multiple(n, multiple):
    return (n - 1) // multiple


def sum_multiples(multiple, max_multiple):
    return multiple * max_multiple * (max_multiple + 1) // 2


if __name__ == '__main__':
    n = 100

    max_multiple_of_3 = find_max_multiple(n, 3)
    max_multiple_of_5 = find_max_multiple(n, 5)
    max_multiple_of_15 = find_max_multiple(n, 15)

    sum_multiples_of_3 = sum_multiples(3, max_multiple_of_3)
    sum_multiples_of_5 = sum_multiples(5, max_multiple_of_5)
    sum_multiples_of_15 = sum_multiples(15, max_multiple_of_15)

    print(sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15)
