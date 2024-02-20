# O(n^2)

def selection_sort(x: list):
    n = len(x)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    return x


if __name__ == '__main__':
    nums = [7, 5, 2, 4, 1, 9, 3]
    print(selection_sort(nums))
