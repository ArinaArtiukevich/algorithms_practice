def main(numbers: list[int], x: int) -> int:
    result = -1
    if len(numbers) > 0:
        for i in range(len(numbers)):
            if numbers[i] == x and result == -1:
                result = i
    return result


if __name__ == '__main__':
    print(main([1, 3,3,3,3], 3))
