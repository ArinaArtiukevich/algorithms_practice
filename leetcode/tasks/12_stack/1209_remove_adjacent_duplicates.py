class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count_letters = []
        for letter in s:
            if count_letters and letter == count_letters[-1][0]:
                count_letters[-1][1] += 1
            else:
                count_letters.append([letter, 1])
            if count_letters[-1][1] == k:
                count_letters.pop()
        result = [letter[0] * letter[1] for letter in count_letters]
        return ''.join(result)


if __name__ == '__main__':
    print(Solution().removeDuplicates(s="deeedbbcccbdaa", k=3))
