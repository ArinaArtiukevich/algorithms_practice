# HINT: Consider each node in the stack having a minimum value.
class MinStack:
    def __init__(self):
        self.stack_min_val = []

    def push(self, val: int) -> None:
       if not self.stack_min_val:
           self.stack_min_val.append([val, val])
       else:
           self.stack_min_val.append([val, val if self.stack_min_val[-1][1] > val else self.stack_min_val[-1][1]])

    def pop(self) -> None:
        self.stack_min_val.pop()

    def top(self) -> int:
        return self.stack_min_val[len(self.stack_min_val) - 1][0]

    def getMin(self) -> int:
        return self.stack_min_val[len(self.stack_min_val) - 1][1]

class MinStackStoringMinVal:
    MAX_VAL = 2 ** 31 - 1

    def __init__(self):
        self.stack = []
        self.current_min = self.MAX_VAL

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min > val:
            self.current_min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.current_min:
            self.current_min = self.MAX_VAL
            for el in self.stack:
                if self.current_min > el:
                    self.current_min = el

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.current_min



if __name__ == '__main__':
    minStack = MinStackStoringMinVal()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
