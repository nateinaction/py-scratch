"""
Binary search of array, look for val
return true if val in arr, else false
"""


def search(arr, val):
    return _search(arr, val, 0, len(arr) - 1)


def _search(arr, val, start, end):
    midpoint = (start + end) // 2

    if start == end:
        return val == arr[midpoint]

    if val > arr[midpoint]:
        # search right
        return _search(arr, val, midpoint + 1, end)
    elif val < arr[midpoint]:
        # search left
        return _search(arr, val, start, midpoint - 1)
    elif val == arr[midpoint]:
        return True


if __name__ == '__main__':
    this_arr = [x for x in range(2)]
    this_val = 2
    print(search(this_arr, this_val))
