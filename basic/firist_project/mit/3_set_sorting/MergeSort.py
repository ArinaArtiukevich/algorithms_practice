import numpy as np


# O(n * log(n))

def merge_sort(x: list):
    if len(x) < 2:
        return x

    mid = len(x) // 2

    left_array = merge_sort(x[:mid])
    right_array = merge_sort(x[mid:])

    return merge_sorted_arrays(left_array, right_array)


def merge_sorted_arrays(x: list, y: list):
    n = len(x) + len(y)
    res = [0] * n
    i, j, k = 0, 0, 0
    while i != len(x) and j != len(y):
        if x[i] < y[j]:
            res[k] = x[i]
            i += 1
        else:
            res[k] = y[j]
            j += 1
        k += 1

    while i != len(x):
        res[k] = x[i]
        k += 1
        i += 1

    while j != len(y):
        res[k] = y[j]
        k += 1
        j += 1
    return res


def merge_sort_pointers(x: list, start: int, end: int):
    if start >= end:
        return

    mid = (start + end) // 2

    merge_sort_pointers(x, start, mid)
    merge_sort_pointers(x, mid + 1, end)

    return merge_sorted_arrays_pointers(x, start, mid, end)


def merge_sorted_arrays_pointers(x: list, start: int, mid: int, end: int):
    i, j, k = 0, 0, start
    z, y = x[start: mid + 1], x[mid + 1: end + 1]
    while i != len(z) and j != len(y):
        if z[i] < y[j]:
            x[k] = z[i]
            i += 1
        else:
            x[k] = y[j]
            j += 1
        k += 1

    while i != len(z):
        x[k] = z[i]
        k += 1
        i += 1

    while j != len(y):
        x[k] = y[j]
        k += 1
        j += 1
    return x


if __name__ == '__main__':
    nums = [7, 5, 2, 4, 1, 9, 3]

    x = [1, 4, 7, 11]
    y = [2, 3, 5, 10]
    print(merge_sort_pointers(nums, 0, len(nums) - 1))
