class Solution:
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        l = 0
        values = set()
        for r in range(0, len(nums)):
            if r - l > k:
                values.remove(nums[l])
                l += 1
            if nums[r] in values:
                return True
            values.add(nums[r])
        return False


if __name__ == '__main__':
    print(Solution().contains_nearby_duplicate(nums=[1,2,3,1,2,3], k=2))
