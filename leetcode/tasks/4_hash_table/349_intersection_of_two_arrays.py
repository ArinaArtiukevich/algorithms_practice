from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_values = set(nums1)
        result = set()
        for num in nums2:
            if num in unique_values:
                result.add(num)
        return list(result)


if __name__ == '__main__':
    print(Solution().intersection(nums1=[2,6,2,9,1], nums2=[7,1]))
