# have a dict and a string
# one letter in a word might be missed
# are all the words in the string present in dict?

# N words in dict
# M words in s
# max(len(word)) = K
# O(N * (K ^ 2)   + M)
def is_word_in_dict(dct: list, s: str):
    words = set(dct)
    wrong_words = set()

    for word in words:
        for i in range(len(word)):
            # create new word O(K)
            # put each symbol O(1)
            words.add(word[:i] + word[i + 1:])
    words = words.union(wrong_words)
    for word in s.split(' '):
        if word not in words:
            return False
    return True


if __name__ == '__main__':
    print(is_word_in_dict(["anagram", 'lol'], 'll loll'))
