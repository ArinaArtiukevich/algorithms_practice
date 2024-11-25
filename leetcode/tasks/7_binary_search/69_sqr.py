class Solution:
    # O(log(n))
    def mySqrt_binary_search(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return l

    # O(n ^ (1/2))
    def mySqrt(self, x: int) -> int:
        prev_val = 0
        val = 0
        while val <= x:
            if val * val == x:
                return val
            if val * val > x:
                return prev_val
            prev_val= val
            val = val + 1
        return val


if __name__ == '__main__':
    print(Solution().mySqrt_binary_search(9))