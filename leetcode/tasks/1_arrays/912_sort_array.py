class Solution:
    def sort_array(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_array = self.sort_array(nums[0:mid])
        right_array = self.sort_array(nums[mid:len(nums)])
        return self.merge_sorted(left_array, right_array)

    def merge_sorted(self, a: list[int], b: list[int]) -> list[int]:
        c = [0 for _ in range(len(a) + len(b))]
        i, j, k = 0, 0, 0
        while i != len(a) and j != len(b):
            if a[i] <= b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
            k += 1
        while i != len(a):
            c[k] = a[i]
            i += 1
            k += 1
        while j != len(b):
            c[k] = b[j]
            j += 1
            k += 1
        return c

    def sort_array_pointers(self, nums: list[int]) -> list[int]:
        return self.sort_array_pointers_recursion(nums, 0, len(nums) - 1)

    def sort_array_pointers_recursion(self, nums: list[int], left: int, right: int) -> list[int]:
        if right <= left:
            return nums
        mid = (left + right) // 2
        self.sort_array_pointers_recursion(nums, left, mid)
        self.sort_array_pointers_recursion(nums, mid + 1, right)
        self.merge_sorted_pointers(nums, left, mid, right)
        return nums

    def merge_sorted_pointers(self, nums: list[int], left: int, mid: int, right: int):
        left_array = nums[left:mid+1]
        right_array = nums[mid+1:right+1]
        i, j, k = 0, 0, left
        while i != len(left_array) and j != len(right_array):
            if left_array[i] <= right_array[j]:
                nums[k] = left_array[i]
                i += 1
            else:
                nums[k] = right_array[j]
                j += 1
            k += 1
        while i != len(left_array):
            nums[k] = left_array[i]
            i += 1
            k += 1
        while j != len(right_array):
            nums[k] = right_array[j]
            j += 1
            k += 1
        return nums


if __name__ == '__main__':
    print(Solution().sort_array_pointers([5, 2, 3, 1]))
