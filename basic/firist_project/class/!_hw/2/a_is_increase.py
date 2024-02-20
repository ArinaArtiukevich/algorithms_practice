def is_increase(elements: list[int]) -> str:
    for i in range(len(elements) - 1):
        if elements[i] >= elements[i + 1]:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    elements = list(map(int, input().split(' ')))
    print(is_increase(elements))