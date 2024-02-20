# min even or -1
def find_min_even_custom(seq: list[int]) -> int:
    # но если ищем нечетные числа?
    # не универсально
    result = -1
    for i in range(len(seq)):
        if not seq[i] % 2 and (result > seq[i] or result == -1):
            result = seq[i]
    return result


def find_min_even_class(seq: list[int]) -> int:
    is_even_met = False
    result = -1
    for i in range(len(seq)):
        if not seq[i] % 2 and (result > seq[i] or not is_even_met):
            result = seq[i]
            is_even_met = True
    return result


if __name__ == '__main__':
    print(find_min_even_class([222, 4, 2, 1, 20, 22]))
