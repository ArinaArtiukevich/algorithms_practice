from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1
        return result[::-1]


if __name__ == '__main__':
    print(Solution().sortedSquares(nums=[-4,-1,0,3,10]))
