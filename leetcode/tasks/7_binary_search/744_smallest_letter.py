from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1

        return letters[l] if letters[l] > target else letters[0]

    def lastSmallestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if letters[mid] >= target:
                r = mid - 1
            else:
                l = mid

        return letters[l]

if __name__ == '__main__':
    print(Solution().lastSmallestLetter(letters = ["c","f","j"], target = "c"))
