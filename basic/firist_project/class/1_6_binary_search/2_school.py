# n people, k parents; # parents so that k + x >= (n + x) * 1/3
def get_parents_number(N: int, k: int) -> int:
    l = 0
    r = N
    while l < r:
        m = (l + r) // 2
        if (k + m) >= (N + m) * 1 / 3:
            r = m
        else:
            l = m + 1
    return l
