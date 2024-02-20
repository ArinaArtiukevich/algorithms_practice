# 2012 vs 1021 yes
# 2012 vs 3102 no

def count_values(x: int) -> list:
    result = [0 for _ in range(10)]
    while x >= 1:
        result[x % 10] += 1
        x //= 10
    return result


def compare_numbers(x: int, y: int) -> bool:
    x_counts, y_counts = count_values(x), count_values(y)
    for i in range(len(x_counts)):
        if x_counts[i] != y_counts[i]:
            return False
    return True


if __name__ == '__main__':
    print(compare_numbers(12901, 91210))
