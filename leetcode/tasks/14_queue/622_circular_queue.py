class CircularQueueArray:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.queue = [0] * self.capacity
        self.head = 0
        self.tail = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.head + self.size) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        self.head = (self.head + 1) % self.capacity
        return True

    def Front(self) -> int:
        return self.queue[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if not self.isEmpty() else -1


class CircularQueueLinkedList:
    class Node:
        def __init__(self, value: int = 0, next: 'Node' = None):
            self.value = value
            self.next = next

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.tail = self.head = None

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.tail.next = self.head
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return True

    def Front(self) -> int:
        return self.head.value if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.value if not self.isEmpty() else -1


if __name__ == '__main__':
    obj = CircularQueueArray(3)
    obj.enQueue(2)
    obj.Rear()
    obj.Front()
    print(obj)
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
