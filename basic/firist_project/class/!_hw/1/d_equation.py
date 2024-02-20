a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
elif (a + b) == c * c:
    print('MANY SOLUTIONS')
elif a == 0:
    print('NO SOLUTION')
elif (c * c - b) / a == (c * c - b) // a:
    print((c ** 2 - b) // a)
else:
    print('NO SOLUTION')

