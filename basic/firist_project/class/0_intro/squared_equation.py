from typing import Optional

from numpy import sqrt


def main(a: int, b: int, c: int) -> Optional[list]:
    result = []
    if a == 0 and b == 0 and c == 0:
        print("infinite number of solutions")
        return None
    elif a == 0 and b == 0:
        result.append(-c)
    elif a == 0 and b != 0:
        result.append(-c/b)
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            result.append((-b) / (2 * a))
        elif d > 0:
            if a > 0:
                result.append((-b + sqrt(d)) / (2 * a))
                result.append((-b - sqrt(d)) / (2 * a))
            else:
                result.append((-b - sqrt(d)) / (2 * a))
                result.append((-b + sqrt(d)) / (2 * a))
    return result


if __name__ == '__main__':
    print(main(-5, 4, 1))

