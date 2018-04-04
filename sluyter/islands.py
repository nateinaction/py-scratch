"""
[10:34 PM] Michael Sluyter: MxN matrix, with either '.' or '#' per cell
[10:35 PM] Michael Sluyter: where '#' represents 'land' and '.' represents water.
Determine the number of discrete islands

EX 1:
.....#....
.....##...
..........
.....#....
..........
##........

Number Islands: 3

EX 2:
.....#....
......#...
..........
.....#....
..........
##........

Number Islands: 4

EX 3:
.....##...
......#...
......#...
.....##...
..####....
###.......

Number Islands: 1

Bonus: Find a solution where you cannot store the entire map in an array. You can store up to sqrt(grid) memory
"""

map1 = """.....#....
.....##...
..........
.....#....
..........
##........"""

map2 = """.....#....
......#...
..........
.....#....
..........
##........"""

map3 = """.....##...
......#...
......#...
.....##...
..####....
###......."""


def find_island_groups(map):
    map_arr = map_to_arr(map)
    len_point = len(map_arr[0])
    len_row = len(map_arr)
    island_count = 0

    for row_i, row in enumerate(map_arr):
        for point_i, point in enumerate(row):
            if point == "#":
                island_count += 1
                map_arr = _find_island_groups(point_i, row_i, len_point, len_row, map_arr, island_count)

    return island_count


def _find_island_groups(point_i, row_i, len_point, len_row, map_arr, island_count):
    # mark as island
    map_arr[row_i][point_i] = island_count

    # check 1. right, 2. down, 3. left, 4. up
    if point_i + 1 < len_point and map_arr[row_i][point_i + 1] == "#":
        map_arr = _find_island_groups(point_i + 1, row_i, len_point, len_row, map_arr, island_count)
    if row_i + 1 < len_row and map_arr[row_i + 1][point_i] == "#":
        map_arr = _find_island_groups(point_i, row_i + 1, len_point, len_row, map_arr, island_count)
    if 0 <= point_i - 1 and map_arr[row_i][point_i - 1] == "#":
        map_arr = _find_island_groups(point_i - 1, row_i, len_point, len_row, map_arr, island_count)
    if 0 <= row_i - 1 and map_arr[row_i - 1][point_i] == "#":
        map_arr = _find_island_groups(point_i, row_i - 1, len_point, len_row, map_arr, island_count)

    return map_arr


def map_to_arr(map):
    return [list(line) for line in map.splitlines()]


if __name__ == '__main__':
    print(find_island_groups(map1))  # expect 3
    print(find_island_groups(map2))  # expect 4
    print(find_island_groups(map3))  # expect 1
