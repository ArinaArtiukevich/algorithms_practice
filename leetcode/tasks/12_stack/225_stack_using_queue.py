class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    my_stak = MyStack()
    my_stak.push(1)
    my_stak.push(2)
    my_stak.push(3)
    print(my_stak.pop())
    print(my_stak.pop())
    print(my_stak.pop())
    print(my_stak.queue)
