# N: [in_i, out_i]; M: boss_j; # boss saw
from typing import List


def get_users(n: int, m: int, t_in: List[int], t_out: List[int], boss: List[int]) -> List[int]:
    current_users = 0
    online_users = []
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    for j in range(m):
        events.append((boss[j], 0))

    # O((2N + M)log(2N + M)) => O(max(N, M)log(max(N, M)))
    events.sort()
    for i in range(len(events)):
        if events[i][1] == -1:
            current_users += 1
        elif events[i][1] == 1:
            current_users -= 1
        else:
            online_users.append(current_users)
    return online_users