from typing import List


class Solution:
    def merge_solution(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda interval: interval[0])
        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if prev_interval[0] <= intervals[i][0] <= prev_interval[1]:
                prev_interval[1] = max(intervals[i][1], prev_interval[1])
            elif prev_interval[1] < intervals[i][0]:
                result.append(prev_interval)
                prev_interval = intervals[i]
        result.append(prev_interval)
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        coordinates = []
        result = []
        cnt = 0
        res_start, res_end = 0, 0
        for interval in intervals:
            coordinates.append([interval[0], -1])
            coordinates.append([interval[1], 1])
        coordinates.sort()
        for coordinate in coordinates:
            if coordinate[1] == -1:
                if cnt == 0:
                    res_start = coordinate[0]
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                result.append([res_start, coordinate[0]])
        return result



if __name__ == '__main__':
    print(Solution().merge_solution(intervals=[[1,4],[2,3]]))
