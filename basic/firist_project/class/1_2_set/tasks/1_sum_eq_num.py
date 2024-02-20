# O(N ^ 2)
def get_pair_sum(nums: list, x: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0


# O(N)
def get_pair_sum_solution(nums: list, x: int):
    reviewed = set()
    for num in nums:
        if x - num in reviewed:
            return num, x - num
        reviewed.add(num)
    return 0, 0


if __name__ == '__main__':
    print(get_pair_sum_solution([5, 3, 1, 6, 12], 9))
