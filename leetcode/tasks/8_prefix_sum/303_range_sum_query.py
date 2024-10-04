from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = self.get_prefix_sum(nums)

    def get_prefix_sum(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        self.prefix_sum = [0] * (len_nums + 2)
        for i in range(len_nums):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]
        return self.prefix_sum


    def sum_range(self, left: int, right: int) -> int:
        print(self.prefix_sum)
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sum_range(2, 5)
    print(param_1)
