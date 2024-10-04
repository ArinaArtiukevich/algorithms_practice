from typing import List


class Solution:
    def pivot_index_total_sum(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            if current_sum == total_sum - current_sum - nums[i]:
                return i
            current_sum = current_sum + nums[i]
        return -1

    def get_prefix_sum(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix_sum = [0] * (len_nums + 1)
        for i in range(len_nums):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        return prefix_sum

    def get_postfix_sum(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        postfix_sum = [0] * (len_nums + 1)
        for i in range(len_nums, 0, -1):
            postfix_sum[i - 1] = postfix_sum[i] + nums[i - 1]
        return postfix_sum

    def pivot_index_sums(self, nums: List[int]) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        postfix_sum = self.get_postfix_sum(nums)
        print(nums, prefix_sum, postfix_sum)
        for i in range(len(nums)):
            if prefix_sum[i + 1] == postfix_sum[i]:
                return i
        return -1

    # time limit error
    def pivot_index(self, nums: List[int]) -> int:
        len_num = len(nums)
        for i in range(len_num):
            left_sum, right_sum = 0, 0
            l, r = i - 1, i + 1
            while l >= 0:
                left_sum += nums[l]
                l -= 1
            while r < len_num:
                right_sum += nums[r]
                r += 1
            if right_sum == left_sum:
                return i
        return -1



if __name__ == '__main__':
    print(Solution().pivot_index_total_sum(nums=[1,7,3,6,5,6]))
