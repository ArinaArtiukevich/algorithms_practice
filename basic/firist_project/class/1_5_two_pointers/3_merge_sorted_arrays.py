from typing import List

def get_merged_arrays(nums_n: List[int], nums_m: List[int]) -> List[int]:
    i_n, i_m = 0, 0
    result = [0] * (len(nums_n) + len(nums_m))
    while i_n < len(nums_n) and i_m < len(nums_m):
        if nums_n[i_n] <= nums_m[i_m]:
            result[i_n + i_m] = nums_n[i_n]
            i_n += 1
        else:
            result[i_n + i_m] = nums_m[i_m]
            i_m += 1
    while i_n < len(nums_n):
        result[i_n + i_m] = nums_n[i_n]
        i_n += 1
    while i_m < len(nums_m):
        result[i_n + i_m] = nums_m[i_m]
        i_m += 1
    return result



if __name__ == '__main__':
    print(get_merged_arrays([1, 3, 5, 7, 8], [2, 3, 4, 10]))
