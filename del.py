
from typing import List


# class Solution:
#     def print_end_time(self, a: int, n: int, t: List[int]):
#         end_time = 0
#         for i in range(n):
#             end_time = max(end_time, t[i])
#             end_time += a
#             print(end_time)
#
# if __name__ == '__main__':
#     n, a = map(int, input().split())
#     t = list(map(int, input().split()))
#
#     Solution().print_end_time(a = a, n = n, t = t)


# class Solution:
#
#     def print_letter_count(self, input_string: str):
#         n = len(input_string)
#         letters = {}
#         substrings = []
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 substrings.append(input_string[i:j])
#         for substring in substrings:
#             for letter in substring:
#                 if letter not in letters:
#                     letters[letter] = 1
#                 else:
#                     letters[letter] += 1
#         for letter in letters:
#             print(letter + ": " + str(letters[letter]))
#
# if __name__ == '__main__':
#     input_string = input()
#     Solution().print_letter_count(input_string=input_string)

# from typing import List

#
# class Solution:
#     MAX_TREE_HEIGHT = 1000000000
#     def get_day(self, n: int, h: List[int], a: List[int], t: List[int]):
#         day = 0
#         while True:
#             updated_h = [h[i] + a[i] * day for i in range(n)]
#             taller_count = [0 for _ in range(n)]
#             for i in range(n):
#                 for j in range(n):
#                     if updated_h[i] < updated_h[j]:
#                         taller_count[i] += 1
#             if taller_count == t:
#                 return day
#             day += 1
#             if any(tree_h > self.MAX_TREE_HEIGHT for tree_h in updated_h) or day > 10000:
#                 return -1
#
#
# if __name__ == '__main__':
#     n_test = int(input())
#     for _ in range(n_test):
#         n = int(input())
#         h = list(map(int, input().split()))
#         a = list(map(int, input().split()))
#         t = list(map(int, input().split()))
#         print(Solution().get_day(n=n, h=h, a=a, t=t))
#
#
# #
#
#
# from typing import List
#
#
# class Solution:
#     def get_max_balanced_m(self, m: int, k: int, b: dict) -> int:
#         sorted_b = sorted(b.items())
#         result = 0
#
#         for _ in range(m):
#             current_subarray = []
#             last_element = None
#             i = 0
#             while i < len(sorted_b):
#                 element, count = sorted_b[i]
#                 if (count > 0 and
#                         (not current_subarray or element - last_element >= k)):
#                     current_subarray.append(element)
#                     last_element = element
#                     b[element] -= 1
#                     if b[element] == 0:
#                         del b[element]
#                     sorted_b = sorted(b.items())
#                     i = 0
#                 else:
#                     i += 1
#             if current_subarray:
#                 result += len(current_subarray)
#
#         return result
#
#
# if __name__ == '__main__':
#     n, m, k = map(int, input().split())
#     b = {}
#     for _ in range(n):
#         a, c = map(int, input().split())
#         b[a] = c
#     print(Solution().get_max_balanced_m(m=m, k=k, b=b))
#
#


from typing import List


class Solution:
    MAX_Y = 1000000
    MIN_Y = 0
    def get_min_dist(self, x: List[int], a: int, b: int) -> int:
        result = float('inf')
        for y in range(self.MIN_Y, self.MAX_Y):
            curr_res = 0
            for x_value in x:
                value = (y - x_value) * a if y >= x_value else (x_value - y) * b
                curr_res += value
            if result > curr_res:
                result = curr_res
        return result



if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print(Solution().get_min_dist(x=x, a=a, b=b))


