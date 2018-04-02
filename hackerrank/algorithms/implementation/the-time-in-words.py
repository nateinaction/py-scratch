# https://www.hackerrank.com/challenges/the-time-in-words/problem

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'half',
}


def timeInWords(h, m):
    if m <= 30:
        hour_words = words[h]
        phrase = ' past '
    else:
        hour_words = words[h + 1]
        phrase = ' to '

    if m > 30:
        minutes = 60 - m
    else:
        minutes = m

    if minutes != 15 and minutes != 30:
        phrase = ' minutes' + phrase

    if 20 < minutes < 30:
        minute_words = words[20] + " " + words[int(str(m)[1])]
    else:
        minute_words = words[minutes]

    if m == 0:
        return hour_words + " o' clock"

    return minute_words + phrase + hour_words


if __name__ == "__main__":
    h = 5
    m = 47
    result = timeInWords(h, m)
    print(result)

    print(timeInWords(1, 31))
    print(timeInWords(12, 30))
    print(timeInWords(9, 45))
