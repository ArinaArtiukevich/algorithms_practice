# O(n^2)

def insertion_sort(x: list):
    n = len(x)
    for i in range(1, n):
        j = i
        while j > 0 and x[j - 1] > x[j]:
            x[j - 1], x[j] = x[j], x[j - 1]
            j -= 1
    return x


if __name__ == '__main__':
    nums = [7, 5, 2, 4, 1, 9, 3]
    print(insertion_sort(nums))
