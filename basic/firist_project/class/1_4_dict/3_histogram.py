# Hello, world!

# sort by symbol code
# print histogram

#
##
##########
# !,Hdelorw

def histogram(s: str) -> str:
    symbols = {}
    max_count = 0
    result = ''
    for symbol in s:
        symbols[symbol] = symbols.get(symbol, 0) + 1
        if max_count < symbols[symbol]:
            max_count = symbols.get(symbol, 0)
    sorted_symbols = sorted(symbols.keys())
    for i in range(max_count, 0, -1):
        current_line = list()
        for key in sorted_symbols:
            if symbols[key] >= i:
                current_line.append('#')
            else:
                current_line.append(' ')
        result = result + ''.join(current_line) + '\n'
    return result + ''.join(sorted_symbols)


if __name__ == '__main__':
    print(histogram('Hello, world!'))
