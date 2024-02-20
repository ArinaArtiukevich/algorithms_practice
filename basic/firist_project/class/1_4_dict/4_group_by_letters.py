# ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

def group_sys_sort(words: list) -> list:
    groups = {}
    result = []
    for word in words:
        # sort words: O(NlogN),
        # if word is long (N) the number of diff letters K <= N
        # => count every letter in N and sort O(KlogK)
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups.keys():
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)
    for sorted_word in groups:
        result.append(groups[sorted_word])
    return result


# IN FACT WORKS SLOWER ON AVERAGE
def sort_letters(word: str) -> str:
    letters = {}
    result = []
    for letter in word:
        if letter not in letters.keys():
            letters[letter] = 0
        letters[letter] += 1
    #     K <= N
    for letter in sorted(letters.keys()):
        result.append(letter)
        result.append(str(letters[letter]))
    return ''.join(result)


def group_sort(words: list) -> list:
    groups = {}
    result = []
    for word in words:
        sorted_word = sort_letters(word)
        if sorted_word not in groups.keys():
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)
    for sorted_word in groups:
        result.append(groups[sorted_word])
    return result


if __name__ == '__main__':
    print(group_sort(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
