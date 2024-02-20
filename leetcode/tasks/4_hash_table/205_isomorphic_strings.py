class Solution:
    def get_map(self, s) -> dict:
        letters = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 0
            letters[s[i]] += i
        return letters

    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters = self.get_map(s)
        t_letters = self.get_map(t)
        for i in range(len(s)):
            if s_letters[s[i]] != t_letters[t[i]]:
                return False
        return True

    def is_isomorphic_solution(self, s: str, t: str) -> bool:
        letters = {}
        adverse = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = t[i]
            if t[i] not in adverse:
                adverse[t[i]] = s[i]
            if letters[s[i]] != t[i] or adverse[t[i]] != s[i]:
                return False
        return True

if __name__ == '__main__':
    print(Solution().is_isomorphic_solution(s="badc", t="baba"))
