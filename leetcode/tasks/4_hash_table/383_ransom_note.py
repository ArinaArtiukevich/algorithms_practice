class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        letters = {}
        for letter in magazine:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        for letter in ransom_note:
            if letter not in letters or letters[letter] - 1 < 0:
                return False
            letters[letter] -= 1
        return True


if __name__ == '__main__':
    print(Solution().can_construct(ransom_note = "aa", magazine = "ab"))

