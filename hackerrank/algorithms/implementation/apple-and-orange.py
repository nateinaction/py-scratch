# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_min, house_max = s, t
    apple_tree, orange_tree = a, b

    print(impactingFruit(house_min, house_max, apple_tree, apples))
    print(impactingFruit(house_min, house_max, orange_tree, oranges))


def impactingFruit(house_min, house_max, fruit_tree, fruits_dropped):
    fruit_hit_house = 0
    for fruit in fruits_dropped:
        if house_min <= fruit + fruit_tree <= house_max:
            fruit_hit_house += 1
    return fruit_hit_house
