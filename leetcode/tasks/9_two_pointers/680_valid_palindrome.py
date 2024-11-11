from typing import List


class Solution:
    def isPalindrome(self, word: List[str]) -> bool:
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        letters = list(s)
        l, r = 0, len(letters) - 1
        while l <= r and letters[l] == letters[r]:
            l += 1
            r -= 1
        if l == r:
            return True
        return self.isPalindrome(word=letters[l+1:r+1]) or self.isPalindrome(word=letters[l:r])



if __name__ == '__main__':
    print(Solution().validPalindrome(s="ccaba"))
