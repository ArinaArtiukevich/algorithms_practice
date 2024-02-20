# use for N values [0, K], K = max - min. K - relatively small

# memory O(K) - new array
# O (N + K). K to create and loop through new array

def count_sort(arr: list) -> list:
    min_value = min(arr) # O(N)
    max_value = max(arr)
    K = max_value - min_value
    count_values = [0 for _ in range(K + 1)]
    for value in arr:
        count_values[value - min_value] += 1
    i = 0
    for j in range(K + 1):
        for k in range(count_values[j]):
            arr[i] = j + min_value
            i += 1
    return arr


if __name__ == '__main__':
    nums = [5, 4, 5, 3, 2, 1, 5]
    print(count_sort(nums))
