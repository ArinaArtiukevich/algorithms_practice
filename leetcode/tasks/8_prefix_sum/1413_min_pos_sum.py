from sys import prefix
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = 1
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < 0 and result <= abs(current_sum):
                result = abs(current_sum) + 1
        return result


if __name__ == '__main__':
    print(Solution().minStartValue(nums=[-3,2,-3,4,2]))