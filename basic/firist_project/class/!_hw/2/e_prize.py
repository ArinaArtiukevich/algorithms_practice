if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split(' ')))

    vasili = 0
    first_position = 0
    for i in range(len(scores)):
        if scores[i] > scores[first_position]:
            first_position = i
    for i in range(first_position + 1, len(scores) - 1):
        if scores[i] % 10 == 5 and scores[i] > scores[i + 1] and scores[i] > vasili:
            vasili = scores[i]

    if vasili == 0:
        print(0)
    else:
        result = 1
        for i in range(len(scores)):
            if scores[i] > vasili:
                result += 1
        print(result)

