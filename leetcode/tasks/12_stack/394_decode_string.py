class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        for char in s:
            if char != ']':
                string_stack.append(char)
            else:
                res_string = ''
                current_string = string_stack.pop()
                while string_stack and not current_string.isdigit() and current_string != '[':
                    res_string = current_string + res_string
                    current_string = string_stack.pop()
                res_num = ''
                while string_stack and string_stack[-1].isdigit():
                    res_num = string_stack.pop() + res_num
                string_stack.append(int(res_num) * res_string)
        result = ''
        for st in string_stack:
            result += st
        return result


if __name__ == '__main__':
    print(Solution().decodeString(s="3[a]2[bc]"))
