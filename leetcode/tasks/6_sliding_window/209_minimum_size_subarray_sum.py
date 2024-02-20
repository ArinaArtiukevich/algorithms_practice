from typing import List


class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        current_sum = 0
        l = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                result = min(result, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return result if result != len(nums) + 1 else 0


if __name__ == '__main__':
    print(Solution().min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]))
