class Solution:

    # memory O(N), time O(n ** 2)
    def length_longest_substring(self, s: str) -> int:
        max_res = 0
        for i in range(len(s)):
            letters = set(s[i])
            curr_res = 1
            for j in range(i + 1, len(s)):
                if s[j] in letters:
                    break
                else:
                    letters.add(s[j])
                    curr_res += 1
            if curr_res > max_res:
                max_res = curr_res
        return max_res

    # memory O(N), time O(n)
    def length_substring_sliding_window(self, s: str) -> int:
        letters = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            result = max(result, len(letters))
        return result


if __name__ == '__main__':
    print(Solution().length_substring_sliding_window('pwwkew'))
