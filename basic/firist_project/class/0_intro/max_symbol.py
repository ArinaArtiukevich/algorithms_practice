def main(string: str) -> str:
    symbol_dict = {}
    result = ''
    max_count = -1
    for symbol in string:
        if symbol in symbol_dict.keys():
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    for key, value in symbol_dict.items():
        if max_count < value:
            max_count = value
            result = key
    return result


# MAX НЕ СРАБОТАЕТ ЕСЛИ ПЕРЕДАДИМ ПУСТУЮ СТРОКУ

def main_1(string: str) -> str:
    symbol_dict = {}
    for symbol in string:
        if symbol in symbol_dict.keys():
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    result = max(symbol_dict, key=symbol_dict.get)
    return result


#

def main_2(string: str) -> str:
    symbol_dict = {}
    max_count = -1
    result = ''
    unique_symbols = set(string)
    for symbol in unique_symbols:
        symbol_dict[symbol] = string.count(symbol)
    for key, value in symbol_dict.items():
        if max_count < value:
            max_count = value
            result = key
    return result


if __name__ == '__main__':
    print(main('arinaaa'))
    s = input().split()
    ints = list(map(int, s))
    print(ints)
    print(s)
