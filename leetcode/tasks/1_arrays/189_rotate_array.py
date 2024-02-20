def rotate_custom_time(nums: list[int], k: int) -> list[int]:
    len_nums = len(nums)
    if k >= len_nums:
        k = k % len_nums
    for i in range(k):
        num = nums[-1]
        for j in range(len_nums - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = num

    return nums


def rotate_custom_accepted_but_memory(nums: list[int], k: int) -> list[int]:
    len_nums = len(nums)
    if k >= len_nums:
        k = k % len_nums

    count_moves = len_nums - k
    nums_to_move = nums[count_moves:]
    nums[count_moves:] = nums[:count_moves]
    nums[:count_moves] = nums_to_move
    return nums


def reverse(nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        nums[r], nums[l] = nums[l], nums[r]
        l, r = l + 1, r - 1
    return nums


def rotate_solution_reversed(nums: list[int], k: int) -> list[int]:
    len_nums = len(nums)
    if k >= len_nums:
        k = k % len_nums
    reverse(nums)
    nums[k:] = reverse(nums[k:])
    nums[:k] = reverse(nums[:k])
    return nums


if __name__ == '__main__':
    print(rotate_solution_reversed([1, 2, 3, 4, 5, 6, 7], 3))
