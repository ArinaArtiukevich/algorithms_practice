# time O(n), memory O(1)
def reverse_string_custom(s: list[str]) -> list[str]:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1
    return s


# STACK, time O(n), memory O(n)
def reverse_string_stack_solution(s: list[str]) -> list[str]:
    stack = []
    for symbol in s:
        stack.append(symbol)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1
    return s


# was not accepted
# recursion, time O(n), memory O(n) (extra space on call stack)
def reverse_string_recursion_solution(s: list[str]) -> list[str]:
    if len(s) == 0:
        return []
    return reverse_string_recursion_solution(s[1:]) + list(s[0])


# 2

def reverse(s: list[str], l: int, r: int):
    if l >= r:
        return
    s[l], s[r] = s[r], s[l]
    reverse(s, l + 1, r - 1)


def reverse_string_recursion_solution_2(s: list[str]) -> list[str]:
    reverse(s, 0, len(s) - 1)
    return s


if __name__ == '__main__':
    print(reverse_string_recursion_solution_2(["h", "e", "l", "l", "o"]))
