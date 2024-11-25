# N tasks; k, k + 1, ...; days ?

def get_total_days(N: int, k: int) -> int:
    l, r = 0, N
    while l < r:
        m = (l + r) // 2 # m - days
        if (k + k + m - 1) * m // 2 >= N:
            r = m
        else:
            l = m + 1
    return l