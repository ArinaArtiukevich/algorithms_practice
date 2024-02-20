# AAABBCCCCDFF -> A5B2C4DF2


# СО СТРОКОЙ РАБОТАТЬ ДОЛГО!
def rle_custom(input: str) -> str:
    result = ''
    if len(input) > 0:
        prev_symbol = input[0]
        counter = 1
        for i in range(1, len(input)):
            if prev_symbol != input[i]:
                result += prev_symbol
                if counter > 1:
                    result += str(counter)
                counter = 1
                prev_symbol = input[i]
            else:
                counter += 1
        result += prev_symbol
        if counter > 1:
            result += str(counter)
    return result


def rle_custom_array(input: str) -> str:
    letters = []
    count_letter = []
    result = ''
    if len(input) > 0:
        prev_symbol = input[0]
        counter = 1
        for i in range(1, len(input)):
            if prev_symbol != input[i]:
                letters.append(prev_symbol)
                count_letter.append(counter)
                counter = 1
                prev_symbol = input[i]
            else:
                counter += 1
        letters.append(prev_symbol)
        count_letter.append(counter)
        for i in range(len(letters)):
            result += letters[i]
            if count_letter[i] > 1:
                result += str(count_letter[i])
    return result


def get_letter_count(symbol: str, count: int) -> str:
    if count > 1:
        return symbol + str(count)
    return symbol


def rle_class(input: str) -> str:
    letters = []
    result = ''
    if len(input) > 0:
        prev_symbol = input[0]
        prev_position = 0
        for i in range(len(input)):
            if prev_symbol != input[i]:
                letters.append(get_letter_count(prev_symbol, i - prev_position))
                prev_position = i
                prev_symbol = input[i]
        letters.append(get_letter_count(prev_symbol, len(input) - prev_position))
        result = ''.join(letters)
    return result


if __name__ == '__main__':
    print(rle_class('AABB   AAACC'))
