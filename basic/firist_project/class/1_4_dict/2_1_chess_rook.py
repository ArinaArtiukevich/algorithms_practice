# N * N - шахматная доска
# M ладей (бьет других по вертикали или горизонтали)
# сколько пар бьют друг друга

# храним количество ладей на вертикали и горизонтали
# n ладей в строке => n - 1 пар

# O(M)
def beat_rook(N: int, roots: []) -> int:
    result = 0
    pos = {}
    for root in roots:
        pos[root[0]] = pos.get(root[0], 0) + 1
        pos[root[1] + N] = pos.get(root[1] + N, 0) + 1
    for key in pos.keys():
        result += pos[key] - 1
    return result


def count_pairs(pos: dict) -> int:
    result = 0
    for key in pos.keys():
        result += pos[key] - 1
    return result


def beat_rook_two_dict(N: int, roots: []) -> int:
    pos_col = {}
    pos_row = {}
    for root in roots:
        pos_row[root[0]] = pos_row.get(root[0], 0) + 1
        pos_col[root[1]] = pos_col.get(root[1], 0) + 1
    return count_pairs(pos_row) + count_pairs(pos_col)


if __name__ == '__main__':
    print(beat_rook_two_dict(5, [[0, 1], [0, 3], [1, 2], [3, 2], [0, 4]]))
