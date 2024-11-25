from typing import List


class Solution:

    def intersection_binary(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = set()
        nums2.sort()
        for num in nums1:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums2[mid] == num:
                    res.add(num)
                    break
                elif nums2[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
        return list(res)


    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                res.add(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return list(res)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(Solution().intersection_binary(nums1=[1,2], nums2=[1,1]))
