"""
Given N, print 1->N
if divisible by 3 print fizz,
if divisible by 5 print buzz,
if divisible by 15 print fizzbuzz
else print N
"""


def fizzbuzz(n, fizz_val, buzz_val):
    text = ''
    for num in range(1, n + 1):
        if num % fizz_val == 0 and num % buzz_val == 0:
            text += "fizzbuzz"
        elif num % fizz_val == 0:
            text += "fizz"
        elif num % buzz_val == 0:
            text += "buzz"
        else:
            text += str(num)

        text += '\n'

    return text


if __name__ == '__main__':
    print(fizzbuzz(25, 3, 7))
