class Solution:
    def is_happy_solution(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.sq_sum(n)
        return False

    def sq_sum(self, n: int) -> int:
        result = 0
        while n / 10 >= 0.1:
            digit = n % 10
            result += digit ** 2
            n = n // 10
        return result



if __name__ == '__main__':
    print(Solution().is_happy_solution(2))
