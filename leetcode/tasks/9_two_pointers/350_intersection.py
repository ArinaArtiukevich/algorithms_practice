from typing import List

class Solution:
    def intersect_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i_1, i_2 = 0, 0
        result = []
        while i_1 != len(nums1) and i_2 != len(nums2):
            if nums1[i_1] < nums2[i_2]:
                i_1 += 1
            elif nums1[i_1] > nums2[i_2]:
                i_2 += 1
            else:
                result.append(nums1[i_1])
                i_1 += 1
                i_2 += 1
        return result


if __name__ == '__main__':
    print(Solution().intersect_sort(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
