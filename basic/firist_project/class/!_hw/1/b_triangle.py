# def is_triangle(a: int, b: int, c: int) -> str:
#     return 'YES' if a + b > c or a + c > b or b + c > a else 'NO'
#
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     print(is_triangle(a, b, c))

a = int(input())
b = int(input())
c = int(input())
print('YES' if (a + b > c) or (a + c > b) or (b + c > a) else 'NO')