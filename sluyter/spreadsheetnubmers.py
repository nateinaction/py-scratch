def to_letter(i):
    n = []
    while i > 0:
        d = chr((i % 26)+64)
        i = i // 26
        n.insert(0, d)
    return "".join(n)


if __name__ == '__main__':
    print(to_letter(1))
