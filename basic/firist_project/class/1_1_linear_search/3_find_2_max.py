from typing import Optional


# max1 and the second max2 values(max if not max1)
# 3, 2, 1, 3 => 3, 3
# N > 1
def find_2_maxes(seq: list[int]) -> Optional[list[int]]:
    result_index = [0, 1]
    for i in range(2, len(seq)):
        if seq[i] > seq[result_index[0]]:
            result_index[1] = result_index[0]
            result_index[0] = i
        elif seq[i] > seq[result_index[1]]:
            result_index[1] = i
    result = [seq[result_index[0]], seq[result_index[1]]]
    return result


# max1 and the second max2 values
# 3, 2, 1, 3 => 3, 2
# N >= 0
def find_2_maxes_2(seq: list[int]) -> Optional[list[int]]:
    if len(seq) >= 2:
        result_index = [0, 1] if seq[0] > seq[1] else [1, 0]
        for i in range(2, len(seq)):
            if seq[i] > seq[result_index[0]]:
                result_index[1] = result_index[0]
                result_index[0] = i
            elif seq[i] > seq[result_index[1]] and seq[i] != seq[result_index[0]]:
                result_index[1] = i
        result = [seq[result_index[0]], seq[result_index[1]]] if seq[result_index[0]] != seq[result_index[1]] else [
            seq[result_index[0]]]
    elif len(seq) == 1:
        result = [seq[0]]
    else:
        result = None
    return result


# max1 and the second max2 values
# 3, 2, 1, 3 => 3, 2
# N >= 0
def find_2_maxes_set(values: list[int]) -> Optional[list[int]]:
    seq = list(set(values))
    if len(seq) >= 2:
        result_index = [0, 1] if seq[0] > seq[1] else [1, 0]
        for i in range(2, len(seq)):
            if seq[i] > seq[result_index[0]]:
                result_index[1] = result_index[0]
                result_index[0] = i
            elif seq[i] > seq[result_index[1]]:
                result_index[1] = i
        result = [seq[result_index[0]], seq[result_index[1]]]
    elif len(seq) == 1:
        result = [seq[0]]
    else:
        result = None
    return result


if __name__ == '__main__':
    print(find_2_maxes_set([1000, 1000, 200, 30000, 30000, 40, 300, 30000]))
