# Given an input file of dictionary words, one per line, and another input file of words to unscramble,
# one per line, print each scrambled word and the corresponding unscrambled word.

scrambled = [
    'sdee',
    'ddpale',
    'rwate',
    'ppael',
    'kcauq',
]

unscrambled = [
    'apple',
    'seed',
    'paddle',
    'quack',
    'water',
]


def unscramble_me(scrambled, unscrambled):
    scrambled_words = {}
    unscrambled_words = {}
    for i in range(len(scrambled)):
        unscrambled_key = sum([ord(char) for char in unscrambled[i]])
        unscrambled_words[unscrambled_key] = unscrambled[i]

        scrambled_key = sum([ord(char) for char in scrambled[i]])
        scrambled_words[scrambled_key] = scrambled[i]

    for key in unscrambled_words:
        print(scrambled_words[key], unscrambled_words[key])


if __name__ == '__main__':
    unscramble_me(scrambled, unscrambled)
