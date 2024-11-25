# non-decreasing order, N, x; first index y: y >= x
from typing import List


def get_index(N: int, seq: List[int], x: int) -> int:
    l, r = 0, N - 1
    while l < r:
        m = (l + r) // 2
        if seq[m] >= x:
            l = m
        else:
            r = m + 1
    return l if seq[l] >= x else N
