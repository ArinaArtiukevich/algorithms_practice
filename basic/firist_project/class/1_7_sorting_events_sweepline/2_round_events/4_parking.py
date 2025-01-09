# N places; M cars: [in_i, out_i]; no places?
from typing import List


def is_occupied(n: int, m: int, t_in: List[int], t_out: List[int], car_size: List[int]) -> bool:
    size_occupied = 0
    events = []
    for i in range(m):
        # while sorting car should first leave then another park
        events.append((t_in[i], 1, car_size[i]))
        events.append((t_out[i],-1, car_size[i]))
    events.sort()
    for i in range(len(events)):
        if events[i][1] == -1:
            size_occupied -= events[i][2]
        else:
            size_occupied += events[i][2]
        if size_occupied == n:
            return True
    return False