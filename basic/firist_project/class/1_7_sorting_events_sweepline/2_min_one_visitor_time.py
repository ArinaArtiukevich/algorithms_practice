# N: [In_i, Out_i]; total time with at least single visitor on the site
from typing import List


def get_visited_time(n: int, t_in: List[int], t_out: List[int]) -> int:
    online_users = 0
    time_online = 0
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    for i in range(len(events)):
        if online_users > 0:
            time_online += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online_users += 1
        else: online_users -= 1
    return time_online