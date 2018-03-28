def is_palindrome(word):
    if not word:
        return False

    midpoint = len(word) // 2
    for i in range(midpoint):
        char1 = word[i]
        char2 = word[-i - 1]
        if char1 != char2:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome("racecar"))
