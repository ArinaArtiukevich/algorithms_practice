from typing import List


def build_prefix_sum(nums: List[int]) -> List[int]:
    prefixsum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefixsum[i + 1] = prefixsum[i] + nums[i]
    return prefixsum

def get_range_sum_query(nums: List[int], left: int, right: int) -> int:
    return nums[right] - nums[left]

if __name__ == '__main__':
    print(get_range_sum_query(build_prefix_sum([1, 2, 3]), 1, 2))
