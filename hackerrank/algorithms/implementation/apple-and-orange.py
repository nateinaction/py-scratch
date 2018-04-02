# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_min, house_max = s, t
    apple_tree, orange_tree = a, b

    apples_hit_tree = 0
    for apple in apples:
        if house_min <= apple + apple_tree <= house_max:
            apples_hit_tree += 1

    oranges_hit_tree = 0
    for orange in oranges:
        if house_min <= orange + orange_tree <= house_max:
            oranges_hit_tree += 1

    print(apples_hit_tree)
    print(oranges_hit_tree)
