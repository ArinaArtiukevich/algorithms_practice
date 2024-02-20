# 1 minute at a station

# first platform: a - between trains, n trains
# second platform: b - between trains, m trains

# min, max time of waiting

if __name__ == '__main__':
    a, b, n, m = int(input()), int(input()), int(input()), int(input())
    t1_min = n + (n - 1) * a
    t1_max = n + (n + 1) * a

    t2_min = m + (m - 1) * b
    t2_max = m + (m + 1) * b

    t_min = max(t1_min, t2_min)
    t_max = min(t1_max, t2_max)

    print(t_min, t_max if t_min <= t_max else -1)



