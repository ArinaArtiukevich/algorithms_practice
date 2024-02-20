def is_simple_palindrome_custom(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


def is_simple_palindrome_recursion_custom(s: str) -> bool:
    if len(s) == 0:
        return True
    is_simple_palindrome_recursion_custom(s[1: -1])
    if s[0] != s[-1]:
        return False


# only characters
def is_palindrome_cheat_solution(s: str) -> bool:
    # additional memory
    new_s = ''
    for symbol in s:
        if symbol.isalnum():
            new_s += symbol.lower()
    # new_s[::-1] additional memory - create new reversed 2_string
    return new_s == new_s[::-1]


def is_alpha_numeric(symbol: str) -> bool:
    # ord(symbol) - ASCII
    return ((ord('A') <= ord(symbol) <= ord('Z')) or
            (ord('a') <= ord(symbol) <= ord('z')) or
            (ord('0') <= ord(symbol) <= ord('9')))


# only characters
# time O(n), memory O(1)
# slow
def is_palindrome_custom_solution(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if is_alpha_numeric(s[l]) and is_alpha_numeric(s[r]):
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        else:
            if not is_alpha_numeric(s[l]):
                l = l + 1
            if not is_alpha_numeric(s[r]):
                r = r - 1
    return True


def is_palindrome_solution(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        # s[l].isalnum() - built-in
        while l < r and not is_alpha_numeric(s[l]):
            l += 1
        while l < r and not is_alpha_numeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def is_palindrome_total_cheat_solution(s: str) -> bool:
    s = (''.join(filter(str.isalnum, str(s))).lower())
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome_total_cheat_solution('A man, a plan, a canal: Panama'))
