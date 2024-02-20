# solution

# a, b, c - brick
# d, e - hole

if __name__ == '__main__':
    brick = []
    for i in range(3):
        brick.append(int(input()))

    for i in range(len(brick) - 1):
        for j in range(len(brick) - 1 - i):
            if brick[j] > brick[i + 1]:
                brick[j], brick[i + 1] = brick[j + 1], brick[i]
    a, b = brick[0], brick[1]

    d = int(input())
    e = int(input())
    if d > e:
        d, e = e, d

    print('YES' if a <= d and b <= e else 'NO')


