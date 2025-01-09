from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        j = 0
        count = 0
        for num in range(left, right+1):
            while num < ranges[j][0] or num > ranges[j][1]:
                j += 1
                if (j >= len(ranges)) or ((j > len(ranges) - 1) and (j == num < ranges[j][0] or num > ranges[j][1])):
                    return False
            if ranges[j][0] <= num <= ranges[j][1]:
                count += 1
        return count == len(range(left, right+1))



if __name__ == '__main__':
    print(Solution().isCovered(ranges=[[15,36],[15,23],[15,44],[30,49],[2,19],[27,36],[7,42],[12,41]], left=19, right=47))
