# N: [In_i, Out_i]; max number of people at the same time
from typing import List


def get_max_visitors(n: int, t_in: List[int], t_out: List[int]) -> int:
    result = 0
    current = 0
    events = []
    for i in range(n):
        # t_in - first so that if t_in[i] == t_out[j] => 2 people counted
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    for event in events:
        if current > result:
            result = current
        current += -event[1]
    return result