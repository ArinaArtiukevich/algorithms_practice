class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        letters = list(s)
        for r in range(len(letters)):
            if letters[r] == ' ' or r == len(letters) - 1:
                p = r - 1 if r != len(letters) - 1 else r
                while l <= p:
                    letters[l], letters[p] = letters[p], letters[l]
                    l += 1
                    p -= 1
                l = r + 1
            r += 1
        return ''.join(letters)

    def reverseWords_long(self, s: str) -> str:
        l, r = 0, 0
        letters = list(s)
        for letter in letters:
            if letter == ' ':
                p = r - 1
                while l <= p:
                    letters[l], letters[p] = letters[p], letters[l]
                    l += 1
                    p -= 1
                l = r + 1
            r += 1
        p = r - 1
        while l <= p:
            letters[l], letters[p] = letters[p], letters[l]
            l += 1
            p -= 1
        return ''.join(letters)



    def reverseWords_split(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            word = list(words[i])
            l, r = 0, len(word) - 1
            while l <= r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            words[i] = ''.join(word)
        return ' '.join(words)


if __name__ == '__main__':
    print(Solution().reverseWords(s="Let's take LeetCode contest"))
