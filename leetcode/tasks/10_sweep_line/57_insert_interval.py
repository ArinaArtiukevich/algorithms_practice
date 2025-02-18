from typing import List

class Solution:

    def insert_solution(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        result = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        result.append(newInterval)
        return result


if __name__ == '__main__':
    print(Solution().insert_solution(intervals = [[1,2]], newInterval = [4,8]))
