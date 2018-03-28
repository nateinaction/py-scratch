"""
Binary search of array, look for range of vals
return any vals in range, else empty array
"""


def search(arr, start_val, end_val):
    start_index = _search(arr, end_val, 0, len(arr) - 1)
    end_index = _search(arr, end_val, 0, len(arr) - 1)

    # I should probably catch if the vals are outside of the array

    return arr[start_index:end_index]


def _search(arr, val, start, end):
    midpoint = (start + end) // 2

    if start == end:
        if val == arr[midpoint]:
            return midpoint

    if val > arr[midpoint]:
        # search right
        return _search(arr, val, midpoint + 1, end)
    elif val < arr[midpoint]:
        # search left
        return _search(arr, val, start, midpoint - 1)
    elif val == arr[midpoint]:
        return midpoint


if __name__ == '__main__':
    this_arr = [x for x in range(9)]
    start_val = 2
    end_val = 5
    print(search(this_arr, start_val, end_val))
