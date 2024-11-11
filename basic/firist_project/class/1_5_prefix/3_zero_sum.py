from typing import List


def count_zero_sum_prefix_sum(nums: List[int]) -> List[int]:
    sums = {0 : 1}
    current_sum = 0
    res = 0
    for num in nums:
        current_sum += num
        if current_sum in sums.keys():
            sums[current_sum] += 1
        else:
            sums[current_sum] = 1
    for key in sums:
        res = res + sums[key] if sums[key] > 1 else res
    return res

def count_zero_sum(nums: List[int]) -> List[int]:
    length = len(nums)
    res = 0
    for right in range(length):
        sum_nums = 0
        for left in range(right, length):
            sum_nums += nums[left]
            if sum_nums == 0:
                res += 1
    return res




if __name__ == '__main__':
    print(count_zero_sum([1, 1, -1, 1, 0, 2, -1, -1]))
