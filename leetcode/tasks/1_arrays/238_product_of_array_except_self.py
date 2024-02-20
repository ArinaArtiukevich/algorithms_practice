class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        prefix = 1
        suffix = 1
        products = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            products[i] = products[i] * prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            products[i] = products[i] * suffix
            suffix *= nums[i]
        return products


if __name__ == '__main__':
    print(Solution().product_except_self([1,2,3,4]))


