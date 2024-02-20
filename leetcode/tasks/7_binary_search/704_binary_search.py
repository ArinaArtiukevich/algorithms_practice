from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursion(nums: List[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_recursion(nums, target, mid + 1, right)
    else:
        return binary_search_recursion(nums, target, left, mid - 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(binary_search_recursion(nums, 5, 0, len(nums) - 1))
