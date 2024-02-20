a1, b1, a2, b2 = map(int, input().split(' '))

squares = {}
squares[max(a1, a2) * (b1 + b2)] = [max(a1, a2), (b1 + b2)]
squares[max(a1, b2) * (b1 + a2)] = [max(a1, b2), (b1 + a2)]
squares[max(b1, a2) * (a1 + b2)] = [max(b1, a2), (a1 + b2)]
squares[max(b1, b2) * (a1 + a2)] = [max(b1, b2), (a1 + a2)]

print(squares[min(squares)][0], squares[min(squares)][1])