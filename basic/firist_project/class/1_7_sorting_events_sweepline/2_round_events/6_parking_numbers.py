# N places; M cars: [in_i, out_i]; numbers of min n cars occupied all places
from typing import List, Set


# introduce set and COPY!(bad) best result every time result in O(M^2) in worst scenario,
# curr_m after each next event - better than prev_m
# each copy => O(M) which might happen ~M times

# better => 2 x for : 1st - find min_m; 2nd - get numbers

# O(MlogM)
def get_numbers(n: int, cars: List) -> Set:
    car_nums = set()
    size_occupied = 0
    n_occupied = 0
    min_occupied = len(cars) + 1
    events = []
    for i in range(len(cars)):
        t_in, t_out, car_size = cars[i]
        events.append((t_in, 1, car_size, i))
        events.append((t_out,-1, car_size, i))
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
    size_occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            size_occupied -= events[i][2]
            n_occupied -= 1
            car_nums.remove(events[i][3])
        else:
            size_occupied += events[i][2]
            n_occupied += 1
            car_nums.add(events[i][3])
        if size_occupied == n and size_occupied == min_occupied:
            return car_nums
    return set()