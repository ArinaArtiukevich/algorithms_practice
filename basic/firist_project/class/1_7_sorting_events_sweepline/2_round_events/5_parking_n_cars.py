# N places; M cars: [in_i, out_i]; min n cars occupied all places
from typing import List


def get_min_n_occupied(n: int, cars: List) -> bool:
    size_occupied = 0
    n_occupied = 0
    min_occupied = len(cars) + 1
    events = []
    for car in cars:
        t_in, t_out, car_size = car
        events.append((t_in, 1, car_size))
        events.append((t_out,-1, car_size))
    events.sort()
    for i in range(len(events)):
        if events[i][1] == -1:
            size_occupied -= events[i][2]
            n_occupied -= 1
        else:
            size_occupied += events[i][2]
            n_occupied += 1
        if size_occupied == n and min_occupied > size_occupied:
            min_occupied = size_occupied
    return min_occupied