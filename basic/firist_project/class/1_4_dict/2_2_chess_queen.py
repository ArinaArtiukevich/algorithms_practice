# same, but + move diagonal
# (P, Q) and (X, Y): P – Q == X – Y or P + Q == X + Y
def count_pairs(pos: dict) -> int:
    result = 0
    for key in pos.keys():
        result += pos[key] - 1
    return result


# def beat_queen(N: int, queens: []) -> int:
#     pos_row = {}
#     pos_col = {}
#
#     pos_left = {}
#     pos_right = {}
#
#     for queen in queens:
#         pos_row[queen[0]] = pos_row.get(queen[0], 0) + 1
#         pos_col[queen[1]] = pos_col.get(queen[1], 0) + 1
#     result = count_pairs(pos_col) + count_pairs(pos_row)
#     return result


def beat_queen(N: int, queens: []) -> int:
    pos_row = {}
    pos_col = {}
    pos_left = {}
    pos_right = {}
    for queen in queens:
        pos_left[queen[0] + queen[1]] = pos_left.get(queen[0] + queen[1], 0) + 1
        pos_right[queen[0] - queen[1]] = pos_right.get(queen[0] - queen[1], 0) + 1
        pos_row[queen[0]] = pos_row.get(queen[0], 0) + 1
        pos_col[queen[1]] = pos_col.get(queen[1], 0) + 1
    return count_pairs(pos_left) + count_pairs(pos_right) + count_pairs(pos_col) + count_pairs(pos_row)


if __name__ == '__main__':
    print(beat_queen(5, [[0, 1], [0, 3], [1, 2], [3, 2], [0, 4], [2, 1]]))
