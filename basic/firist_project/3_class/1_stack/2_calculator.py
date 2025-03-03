class SimpleSolution:
    VALID_OPERATION = ['+', '-', '*', '/']

    def calculate_stack(self, input: str) -> int:
        n = len(input)
        number_stack = []
        current_number = 0
        current_operator = '+'
        for i, char in enumerate(input):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if char in self.VALID_OPERATION or i == n - 1:
                if current_operator == '+':
                    number_stack.append(current_number)
                elif current_operator == '-':
                    number_stack.append((-1) * current_number)
                elif current_operator == '*':
                    number_stack.append(number_stack.pop() * current_number)
                elif current_operator == '/':
                    number_stack.append(int(number_stack.pop() / current_number))
                current_number = 0
                current_operator = char
        return sum(number_stack)

    def calculate(self, input: str) -> int:
        n = len(input)
        result = 0
        prev_num, current_num = 0, 0
        current_operator = '+'
        for i, char in enumerate(input):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            if char in self.VALID_OPERATION or i == n - 1:
                match current_operator:
                    case '+':
                        result += prev_num
                        prev_num = current_num
                    case '-':
                        result += prev_num
                        prev_num = -current_num
                    case '*':
                        prev_num *= current_num
                    case '/':
                        prev_num = int(prev_num / current_num)
                current_num = 0
                current_operator = char
        return result + prev_num


class ParenthesisSolution:
    TOP_PRIORITY = ['*', '/']
    LOW_PRIORITY = ['+', '-']
    VALID_PARENTHESIS = ['(', ')']

    def calculate(self, input: str) -> int:
        digits = []

        input = input.replace(' ', '')
        if input[0] == '-':
            input = '0' + input
        prn = self._get_RPN(input)
        for char in prn:
            if str(char).isdigit():
                digits.append(int(char))
            else:
                a = digits.pop()
                b = digits.pop()
                digits.append(self._calculate_single_operation(char, a, b))
        return digits[0]

    def _get_RPN(self, input: str) -> list:
        result = []
        operands = []
        for char in input:
            if char.isdigit():
                result.append(int(char))
            elif char in self.TOP_PRIORITY or char in self.LOW_PRIORITY or char in self.VALID_PARENTHESIS:
                if char == self.VALID_PARENTHESIS[0]:
                    operands.append(char)
                elif char in self.LOW_PRIORITY or char in self.TOP_PRIORITY:
                    while operands and operands[-1] in self.TOP_PRIORITY:
                        result.append(operands.pop())
                    operands.append(char)
                elif char == self.VALID_PARENTHESIS[1]:
                    while operands[-1] != self.VALID_PARENTHESIS[0]:
                        result.append(operands.pop())
                    operands.pop()
        while operands:
            result.append(operands.pop())
        return result

    def _calculate_single_operation(self, operation: str, a: int, b: int) -> int:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return int(a / b)
        return -1


if __name__ == '__main__':
    print(ParenthesisSolution().calculate("6+3*(1+4*5)*2"))
