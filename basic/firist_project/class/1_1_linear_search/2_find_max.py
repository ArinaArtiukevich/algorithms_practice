from typing import Optional


# N > 0
def find_max(numbers: list[int]) -> int:
    result = numbers[0]
    for i in range(len(numbers)):
        if result < numbers[i]:
            result = numbers[i]
    return result


# N >= 0
def find_max_1(numbers: list[int]) -> Optional[int]:
    if len(numbers) == 0:
        result = None
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            if result < numbers[i]:
                result = numbers[i]
    return result


# строки и др сравниваемые объекты
def find_max_2(seq: list[int]) -> Optional[int]:
    if len(seq) == 0:
        result = None
    else:
        index_max = 0
        for i in range(1, len(seq)):
            if seq[index_max] < seq[i]:
                # в питоне работаем через ссылки
                # но лучше запоминать ссылки тк мб полное копирование объекта в др языках

                # но с обращением по индексу мб дольше по времени
                index_max = i
        result = seq[index_max]
    return result


if __name__ == '__main__':
    print(find_max_1([]))
