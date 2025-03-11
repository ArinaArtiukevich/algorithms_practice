from pandas.core.computation.common import result_type_many


class Solution:
    # non recursive
    def myPow_loop(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = result * x
                n -= 1
            x = x * x
            n = n / 2
        return result

    # O(logN)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        result = self.myPow(x * x, n // 2)
        if n % 2 == 1:
            return result * x
        else:
            return result

    # O(n)
    def myPow_n_complexity(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return self.myPow_n_complexity(x, n - 1) * x
        elif n < 0:
            return self.myPow_n_complexity(x, n + 1) / x


if __name__ == '__main__':
    print(Solution().myPow_loop(x=2, n=10))
