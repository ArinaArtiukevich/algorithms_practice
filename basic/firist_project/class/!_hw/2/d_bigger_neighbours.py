if __name__ == '__main__':
    elements = list(map(int, input().split(' ')))
    result = 0
    for i in range(1, len(elements) - 1):
        if elements[i - 1] < elements[i] > elements[i + 1]:
            result += 1
    print(result)



