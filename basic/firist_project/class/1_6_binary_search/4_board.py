# board - W * H; N - square notes
def get_square_side(W: int, H: int, N: int) -> int:
    l = 1
    r = W if W > H else H
    while l < r:
        m = (l + r + 1) // 2
        if N <= (W // m) * (H // m):
            l = m
        else:
            r = m - 1
    return l
