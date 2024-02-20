class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        result = curr_sum
        left = 0
        for right in range(k, len(nums)):
            curr_sum -= nums[left]
            curr_sum += nums[right]
            left += 1
            result = max(result, curr_sum)
        return result / k


if __name__ == '__main__':
    print(Solution().find_max_average(nums=[5], k=1))
