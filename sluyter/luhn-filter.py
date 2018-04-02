def is_valid(cc_num):
    total = 0
    for i, num in enumerate(reversed(cc_num), 1):
        if i % 2 == 0:
            total += sum((int(x) for x in str(num * 2)))
        else:
            total += num

    return total % 10 == 0


if __name__ == '__main__':
    cc_input = [1, 2, 3, 4, 5, 6, 6]
    print(is_valid(cc_input))

    cc_input = [1, 2, 3, 4, 5, 6, 7]
    print(is_valid(cc_input))
