import math

# A kit is a set of lego-like blocks of various sizes, in various amounts.
# This maps size -> num_blocks
kit = {
    '1x1': 3,
    '2x2': 3,
    '2x4': 4,
    '1x8': 2,
    '4x4': 1
}


def num_kits(requirements):
    """Given a set of requirements (map) return the number of kits required to satisfy"""
    max_kits_req = 0
    for block_type in requirements:
        kits_req = math.ceil(requirements[block_type] / kit[block_type])
        max_kits_req = max(max_kits_req, kits_req)
    print(max_kits_req)


if __name__ == '__main__':
    telephone_pole = {
        '1x1': 13
    }
    num_kits(telephone_pole)

    block = {
        '4x4': 4
    }
    num_kits(block)

    house = {
        '2x2': 8,
        '2x4': 6,
        '4x4': 2,
        '1x1': 1
    }
    num_kits(house)

    castle = {
        '1x1': 2,
        '2x2': 17,
        '2x4': 12,
        '1x8': 11,
        '4x4': 4
    }
    num_kits(castle)

    airport = {
        '1x1': 19,
        '2x2': 12,
        '2x4': 13,
        '1x8': 17,
        '4x4': 5
    }
    num_kits(airport)

