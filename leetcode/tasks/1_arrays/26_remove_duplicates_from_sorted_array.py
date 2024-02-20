def remove_duplicates_custom(nums: list) -> (int, list):
    k = 0
    if len(nums) > 0:
        prev_number = nums[0]
        k += 1
        for i in range(1, len(nums)):
            if prev_number != nums[i]:
                nums[k] = nums[i]
                prev_number = nums[i]
                k += 1
                if k - 1 != i:
                    nums[i] = ''
            else:
                nums[i] = ''
        if k < len(nums):
            nums[-1] = ''
    return (k, nums)


def remove_duplicates_improved(nums: list[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == '__main__':
    print(remove_duplicates_improved([1, 1, 1, 1, 2, 2, 2, 2, 3, 3]))