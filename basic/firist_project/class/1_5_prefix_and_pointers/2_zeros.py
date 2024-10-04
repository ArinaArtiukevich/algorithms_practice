# m requests
# O(NM) - перебор всех элементов и подсчет нулей
from typing import List

# O(N + M)
def build_zeros_count(nums: List[int]) -> List[int]:
    prefixzeroes = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefixzeroes[i + 1] = prefixzeroes[i] + 1 if nums[i] == 0 else prefixzeroes[i]
    return prefixzeroes

def count_zeros(prefixzeroes: List[int], left: int, right: int) -> int:
    return prefixzeroes[right] - prefixzeroes[left]

if __name__ == '__main__':
    print(count_zeros(build_zeros_count([0, 0, 2, 0]), 1, 2))
