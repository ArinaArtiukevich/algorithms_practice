from typing import List


class Solution:
    def single_number_bit(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def single_number(self, nums: List[int]) -> int:
        count_nums = {}
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1
        for key in count_nums.keys():
            if count_nums[key] == 1:
                return key
        return -1



if __name__ == '__main__':
    print(Solution().single_number_bit(nums=[2,2,1]))
