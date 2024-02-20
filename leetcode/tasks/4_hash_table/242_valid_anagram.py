class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in t:
            if letter not in letters.keys():
                return False
            letters[letter] = letters[letter] - 1
        for letter in letters:
            if letters[letter] != 0:
                return False
        return True

    def is_anagram_solution(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            letters_s[s[i]] = letters_s.get(s[i], 0) + 1
            letters_t[t[i]] = letters_t.get(t[i], 0) + 1
        for k_s in letters_s:
            if letters_s[k_s] != letters_t.get(k_s, 0):
                return False
        return True

    def is_anagram_solution_cheat(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(Solution().is_anagram_solution("anagram", "nagaram"))
