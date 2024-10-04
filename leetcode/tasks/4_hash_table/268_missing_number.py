from typing import List


class Solution:
    def missing_number_bit(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res + i + 1
            res = res - nums[i]
        return res

    def missing_number(self, nums: List[int]) -> int:
        num_len = len(nums)
        existing_nums = [0] * (num_len + 1)
        for num in nums:
            existing_nums[num] += 1
        for i in range(num_len + 1):
            if existing_nums[i] == 0:
                return i
        return -1



if __name__ == '__main__':
    print(Solution().missing_number_bit(nums=[9,6,4,2,3,5,7,0,1]))
