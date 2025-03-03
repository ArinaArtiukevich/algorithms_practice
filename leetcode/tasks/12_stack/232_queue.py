class MyQueue:

    def __init__(self):
        self.queue = []
        self.reversed_queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.reversed_queue) == 0:
            while self.queue:
                self.reversed_queue.append(self.queue.pop())
        return self.reversed_queue.pop()

    def peek(self) -> int:
        return self.reversed_queue[len(self.reversed_queue) - 1] if len(self.reversed_queue) > 0 else self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0 and len(self.reversed_queue) == 0

    def _push_n_complexity(self, x: int) -> None:
        self.queue.append(x)

    def _pop_n_complexity(self) -> int:
        while len(self.queue) > 1:
            self.reversed_queue.append(self.queue.pop())
        result = self.queue.pop()
        while self.reversed_queue:
            self.queue.append(self.reversed_queue.pop())
        return result


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(8)
    print(obj.pop())
    obj.push(3)
    print(obj.peek())
    # obj.push(5)
    # obj.pop()


    # obj.push(1)
    # obj.push(2)
    # print(obj.peek())
    # obj.push(3)
    # print(obj.pop())
    # obj.push(4)
    # obj.push(5)
    # print(obj.pop())
    # obj.push(6)
    #
    # print(obj.pop())
    # print(obj.empty())
