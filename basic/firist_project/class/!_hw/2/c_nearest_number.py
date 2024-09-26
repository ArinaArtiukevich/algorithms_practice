if __name__ == '__main__':
    n = int(input())
    elements = list(map(int, input().split(' ')))
    x = int(input())

    prev_diff = 2001
    result = 1001

    for element in elements:
        diff = x - element if (x - element) > 0 else -(x - element)
        if diff < prev_diff:
            prev_diff = diff
            result = element
    print(result)
