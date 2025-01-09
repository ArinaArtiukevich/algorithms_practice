from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 1950 - 2050
        years = [0] * 101
        pop = 0
        max_pop = 0
        best_year = 0
        for log in logs:
            years[log[0]-1950] += 1
            years[log[1]-1950] -= 1
        for i in range(101):
            pop += years[i]
            if max_pop < pop:
                max_pop = pop
                best_year = 1950 + i
        return best_year



    def maximumPopulation_custom(self, logs: List[List[int]]) -> int:
        best_cnt = 0
        current_cnt = 0
        best_year = 0
        dates = []
        for log in logs:
            dates.append([log[0], -1])
            dates.append([log[1]-1, 1])
        dates.sort()
        for date in dates:
            if date[1] == -1:
                current_cnt += 1
            else:
                current_cnt -= 1
            if best_cnt < current_cnt:
                best_cnt = current_cnt
                best_year = date[0]
        return best_year



if __name__ == '__main__':
    print(Solution().maximumPopulation(logs=[[1950,1961],[1960,1971],[1970,1981]]))
