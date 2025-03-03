# for any x_i find j: x_i > x_j and i < j

class SmallestRight:

    def get_smallest_right_ids(self, input: list[int]) -> list[list]:
        result = []
        numbers_stack = []
        for i, num in enumerate(input):
            while numbers_stack and numbers_stack[-1][1] > num:
                current_value = numbers_stack.pop()
                current_value.append(i)
                result.append(current_value)
            else:
                numbers_stack.append([i, num])
        while numbers_stack:
            current_value = numbers_stack.pop()
            current_value.append(len(input))
            result.append(current_value)
        return result



if __name__ == '__main__':
    print(SmallestRight().get_smallest_right_ids([7, 2, 4, 5, 3, 2, 5, 1, 5, 4]))
