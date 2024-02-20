class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        string_arr = s.split(' ')
        if len(pattern) != len(string_arr):
            return False
        pattern_count = {}
        string_count = {}
        for i in range(len(pattern)):
            pattern_count[pattern[i]] = pattern_count.get(pattern[i], [])
            pattern_count[pattern[i]].append(i)
            string_count[string_arr[i]] = string_count.get(string_arr[i], [])
            string_count[string_arr[i]].append(i)
        if len(pattern_count) != len(string_count):
            return False
        for string_values, pattern_values in zip(string_count.values(), pattern_count.values()):
            if string_values != pattern_values:
                return False
        return True

    def word_pattern_solution(self, pattern: str, s: str) -> bool:
        string_arr = s.split(' ')
        if len(pattern) != len(string_arr):
            return False
        letter_count = {}
        word_count = {}
        for word, letter in zip(string_arr, pattern):
            if word in word_count and word_count[word] != letter:
                return False
            if letter in letter_count and letter_count[letter] != word:
                return False
            letter_count[letter] = word
            word_count[word] = letter
        return True


if __name__ == '__main__':
    print(Solution().word_pattern("abba", "dog cat cat dog"))
