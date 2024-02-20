def qs(nums: list[int], left: int, right: int) -> list[int]:
    if right <= left:
        return nums
    p = partition(nums, left, right)
    qs(nums, left, p - 1)
    qs(nums, p + 1, right)
    return nums


def partition(nums: list[int], left: int, right: int) -> int:
    i = left - 1
    p = right
    for j in range(left, right):
        if nums[j] < nums[p]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[p], nums[i + 1] = nums[i + 1], nums[p]
    return i + 1


if __name__ == '__main__':
    nums = [7, 5, 2, 4, 1, 9, 3]
    print(qs(nums, 0, len(nums) - 1))
