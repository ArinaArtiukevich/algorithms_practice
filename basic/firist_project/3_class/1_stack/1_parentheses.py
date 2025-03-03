class Solution:
    def is_valid_parentheses_count(self, input: str) -> bool:
        count = 0
        for char in input:
            if char == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def is_valid_diff_parentheses_count(self, input: str) -> bool:
        stack = []
        parentheses_dict = {'(': ')', '{': '}', '[': ']'}
        open_par = ['(', '{', '[']
        close_par = [')', '}', ']']
        for char in input:
            if char in open_par:
                stack.append(char)
            elif char in close_par and len(stack) != 0:
                prev_char = stack.pop()
                if parentheses_dict[prev_char] != char:
                    return False
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().is_valid_parentheses_count(")"))