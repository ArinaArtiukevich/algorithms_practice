from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        count_nums = {}
        result, result_count = 0, 0
        for num in nums:
            if num in count_nums.keys():
                count_nums[num] += 1
            else:
                count_nums[num] = 1

        for k in count_nums:
            if result_count < count_nums[k]:
                result = k
                result_count = count_nums[k]
        return result

    def majority_element_updated(self, nums: List[int]) -> int:
        count_nums = {}
        result, result_count = 0, 0
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1
            if result_count < count_nums[num]:
                result_count = count_nums[num]
                result = num
        return result



if __name__ == '__main__':
    print(Solution().majority_element_updated([3, 2, 3]))
