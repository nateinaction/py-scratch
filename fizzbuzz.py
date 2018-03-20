"""
Given N, print 1->N
if divisible by 3 print fizz,
if divisible by 5 print buzz,
if divisible by 15 print fizzbuzz
else print N
"""


def fizzbuzz(n, fizz_val, buzz_val):
    for num in range(1, n + 1):
        text = ''
        if num % fizz_val == 0:
            text += "fizz"
        if num % buzz_val == 0:
            text += "buzz"

        if not text:
            text += str(num)

        print(text)


if __name__ == '__main__':
    fizzbuzz(25, 3, 7)
