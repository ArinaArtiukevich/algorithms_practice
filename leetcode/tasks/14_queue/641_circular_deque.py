class Node:
    def __init__(self, val: int = 0, prev: 'Node' = None, next: 'Node' = None):
        self.value = val
        self.prev = prev
        self.next = next

class CircularDequeDLL:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1

        temp = Node(value)
        temp.next = self.head.next
        temp.prev = self.head
        self.head.next.prev = temp
        self.head.next = temp
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        temp = Node(value)
        temp.next = self.tail
        temp.prev = self.tail.prev
        self.tail.prev.next = temp
        self.tail.prev = temp
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return True

    def getFront(self) -> int:
        return self.head.next.value if self.size > 0 else -1

    def getRear(self) -> int:
        return self.tail.prev.value if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == '__main__':
    obj = CircularDequeDLL(3)
    obj.insertLast(1)
    obj.insertLast(2)
    obj.insertFront(3)

    obj.insertFront(4)
    obj.deleteLast()
    obj.deleteFront()

    print(obj)
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()
