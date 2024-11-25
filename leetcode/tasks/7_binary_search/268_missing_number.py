from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

if __name__ == '__main__':
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))