from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        m, n = m - 1, n - 1
        current = len(nums1) - 1
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[current] = nums1[m]
                m -= 1
            else:
                nums1[current] = nums2[n]
                n -= 1
            current -= 1
        while m > -1:
            nums1[current] = nums1[m]
            m -= 1
            current -= 1
        while n > -1:
            nums1[current] = nums2[n]
            n -= 1
            current -= 1
        return nums1

    def merge_recursion(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        m, n = m - 1, n - 1
        current = len(nums1) - 1
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[current] = nums1[m]
                m -= 1
            else:
                nums1[current] = nums2[n]
                n -= 1
            current -= 1
        while m > -1:
            nums1[current] = nums1[m]
            m -= 1
            current -= 1
        while n > -1:
            nums1[current] = nums2[n]
            n -= 1
            current -= 1
        return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(Solution().merge(nums1, m, nums2, n))
