# Given a file, print out last n lines of file. File can be arbitrarily large.
# Bonus: implement circular buffer. DONE!

import os


def tail(filename, num_lines = 10):
    filename = os.path.expanduser(filename)
    last_n_lines = ["" for _ in range(10)]
    index = 0
    with open(filename) as f:
        for line in f:
            last_n_lines[index] = line
            index = 0 if index == num_lines - 1 else index + 1

    print("".join(last_n_lines[index:] + last_n_lines[:index]))


if __name__ == '__main__':
    tail("./islands.py")
