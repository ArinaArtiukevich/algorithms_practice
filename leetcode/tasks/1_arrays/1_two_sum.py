def two_sum_custom_slow(nums: list[int], target: int) -> list[int]:
    result = []
    is_found = False
    for i in range(len(nums)):
        if not is_found:
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    is_found = True
                    break
        else:
            break
    return result


def two_sum_solution(nums: list[int], target: int) -> list[int]:
    elements = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in elements.keys():
            return [elements[diff], i]
        elements[num] = i
    return []


if __name__ == '__main__':
    print(two_sum_solution([1, 4, 2], 3))
