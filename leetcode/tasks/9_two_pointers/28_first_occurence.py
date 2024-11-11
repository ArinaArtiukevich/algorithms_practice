class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i_h, i_n  = 0, 0
        result = -1
        while i_h <= len(haystack) - len(needle) + 1 and result == -1:
            i_n = 0
            while i_n != len(needle) and haystack[i_h + i_n] == needle[i_n]:
                i_n += 1
            if i_n == len(needle):
                result = i_h
            i_h += 1
        return result




if __name__ == '__main__':
    print(Solution().strStr(haystack = "aaa", needle = "aaaa"))
