class Solution:
    def first_uniq_char(self, s: str) -> int:
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1



if __name__ == '__main__':
    print(Solution().first_uniq_char(s="leetcode"))
