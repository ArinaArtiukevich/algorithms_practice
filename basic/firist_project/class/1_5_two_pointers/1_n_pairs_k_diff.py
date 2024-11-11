# nums - sorted!; N A, B: A - B > K

from typing import List

def get_n_pairs_solution(nums: List[int], k: int) -> int:
    result = 0
    len_nums = len(nums)
    l, r = 0, 0

    for l in range(len_nums):
        while r < len_nums and nums[r] - nums[l] <= k:
            r += 1
        result += len_nums - r
    return result


def get_n_pairs_optimized(nums: List[int], k: int) -> int:
    result = 0
    len_nums = len(nums)
    l, r = 0, 0
    while r < len_nums and nums[r] - nums[l] <= k:
        r += 1
    while l < len_nums and r < len_nums:
        if nums[r] - nums[l] > k:
            result += len_nums - r
            l += 1
        else:
            r += 1
    return result

# still O(N^2) in the worst case
def get_n_pairs_less_iterations(nums: List[int], k: int) -> int:
    result = 0
    len_nums = len(nums)
    l, r = 0, 0
    while l < len_nums:
        r = l
        while r < len_nums:
            if nums[r] - nums[l] > k:
                result += len_nums - r
                r = len_nums
            r += 1
        l += 1
    return result

def get_n_pairs(nums: List[int], k: int) -> int:
    result = 0
    len_nums = len(nums)
    l, r = 0, 0
    while l < len_nums:
        r = l
        while r < len_nums:
            if nums[r] - nums[l] > k:
                result += 1
            r += 1
        l += 1
    return result



if __name__ == '__main__':
    print(get_n_pairs_solution([1, 3, 5, 7, 8], 20))
