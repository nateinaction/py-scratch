def is_valid(cc_num):
    sum_me = []
    for i, num in enumerate(reversed(cc_num)):
        if (i + 1) % 2 == 0:
            for doubled_num in str(num * 2):
                sum_me.append(int(doubled_num))
        else:
            sum_me.append(num)

    if sum(sum_me) % 10 == 0:
        return True
    return False


if __name__ == '__main__':
    cc_input = [1, 2, 3, 4, 5, 6, 6]
    print(is_valid(cc_input))

    cc_input = [1, 2, 3, 4, 5, 6, 7]
    print(is_valid(cc_input))
