from typing import List


class Solution:
    def longest_consecutive_solution(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in set_nums:
                current_len = 0
                while num + current_len in set_nums:
                    current_len += 1
                result = max(result, current_len)
        return result



if __name__ == '__main__':
    print(Solution().longest_consecutive_solution(nums=[100, 4, 200, 1, 3, 2]))
