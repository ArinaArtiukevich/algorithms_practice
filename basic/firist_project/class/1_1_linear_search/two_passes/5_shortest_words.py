# можно за один проход, но нужно сразу запоминать последовательности коротких слов
# если встретили меньшую длину убирать все и записывать заново => медленно, не разумное использование памяти

# НЕТ ИСПОЛЬЗВАТЬ МАССИВ СНАЧАЛА ВМЕСТО СТРОКИ
# строка  неизменяемая => каждый раз создаем новую строку
def get_shortest_words_custom(seq: list[str]) -> str:
    result = ''
    if len(seq) == 0:
        result = None
    else:
        min_len = len(seq[0])
        for i in range(1, len(seq)):
            if len(seq[i]) < min_len:
                min_len = len(seq[i])
        for i in range(len(seq)):
            if len(seq[i]) == min_len:
                result += seq[i] + ' '
    return result


def get_shortest_words_class(seq: list[str]) -> str:
    if len(seq) == 0:
        result = None
    else:
        shortest_words = []
        min_len = len(seq[0])
        for i in range(1, len(seq)):
            if len(seq[i]) < min_len:
                min_len = len(seq[i])
        for i in range(len(seq)):
            if len(seq[i]) == min_len:
                # О(1)
                shortest_words.append(seq[i])
        result = ' '.join(shortest_words)
    return result


if __name__ == "__main__":
    print(get_shortest_words_class(['va', 'va', 's', 'bv']))
