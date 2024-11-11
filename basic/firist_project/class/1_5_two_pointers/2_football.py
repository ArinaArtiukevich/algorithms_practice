# scores - sorted!; find max sum(scores): any score A, B, C: A <= B + C.

from typing import List

def get_max_scores_sum(nums: List[int]) -> int:
    result, curr_sum = 0, 0
    len_nums = len(nums)
    r, l = 0, 0
    for l in range(len_nums):
        curr_sum = nums[l]
        while r < len_nums and (r == l or nums[r] <= nums[l + 1] + nums[l]):
            curr_sum += nums[r]
            r += 1
        if curr_sum > result:
            result = curr_sum
        curr_sum -= nums[l]
    return result



if __name__ == '__main__':
    print(get_max_scores_sum([1, 3, 5, 7, 8]))
