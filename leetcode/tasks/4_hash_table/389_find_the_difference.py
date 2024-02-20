class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        letters = {}
        for letter in t:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        for letter in s:
            letters[letter] -= 1
        for letter in letters:
            if letters[letter] != 0:
                return letter


    def create_map(self, s) -> dict:
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        return letters

    def find_the_difference_maps(self, s: str, t: str) -> str:
        letters_s, letters_t = self.create_map(s), self.create_map(t)
        for letter in letters_t:
            if letter not in letters_s or letters_t[letter] != letters_s[letter]:
                return letter

    def find_the_difference_sort(self, s: str, t: str) -> str:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        for i in range(len(t_sorted)):
            if i == len(s_sorted) or s_sorted[i] != t_sorted[i]:
                return t_sorted[i]

    def count_letters(self, s: str) -> list[int]:
        result = [0 for i in range(26)]
        K = 97
        for letter in s:
            result[ord(letter) - K] += 1
        return result

    def find_the_difference_custom_sort(self, s: str, t: str) -> str:
        s_count = self.count_letters(s)
        t_count = self.count_letters(t)
        for i in range(len(t_count)):
            if s_count[i] != t_count[i]:
                return chr(97 + i)


    def find_the_difference_ascii_sum(self, s: str, t: str) -> str:
        sum_s, sum_t = 0, 0
        for i in range(len(s)):
            sum_s += ord(s[i])
            sum_t += ord(t[i])
        sum_t += ord(t[len(t) - 1])
        return chr(sum_t - sum_s)

    def find_the_difference_bit(self, s: str, t: str) -> str:
        result = 0
        for letter in s:
            result = result ^ ord(letter)
        for letter in t:
            result = result ^ ord(letter)
        return chr(result)


if __name__ == '__main__':
    print(Solution().find_the_difference_bit(s="abcd", t="abcde"))
