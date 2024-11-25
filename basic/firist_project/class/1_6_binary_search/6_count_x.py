# non-decreasing order, N, x; find # x
from typing import List

def check_l_index(seq: List[int], x: int, m: int):
    return seq[m] >= x

def check_r_index(seq: List[int], x: int, m: int):
    return seq[m] > x

def lbs(N: int, seq: List[int], x: int, check) -> int:
    l, r = 0, N - 1
    while l < r:
        m = (l + r) // 2
        if check(seq, x, m):
            l = m
        else:
            r = m + 1
    return l if check(seq, x, l) else N


def get_index(N: int, seq: List[int], x: int) -> int:
    return lbs(N, seq, x, check_r_index) - lbs(N, seq, x, check_l_index)

